"""Fetch the NYC 311 aggregates Module 7 needs, once, and freeze them.

Usage (from the project root): python data/fetch_nyc311.py

Source: NYC Open Data, "311 Service Requests from 2020 to Present" (dataset erm2-nwe9),
public, no login. Only aggregates are fetched (a few thousand rows), never raw records.

The first run writes data/raw/nyc311/*.csv plus manifest.json (fetch time and a SHA-256 per
file). Later runs do not fetch again; they check the files against the manifest. The city
revises this dataset over time, so a fresh fetch (delete data/raw/nyc311/) can give slightly
different numbers; the manifest makes that visible instead of silent.
"""
import csv
import hashlib
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent / "raw" / "nyc311"
BASE = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
LABELS = "complaint_type in('Water System','Sewer','Water Maintenance','Sewer Maintenance')"
AUG = lambda y: f"created_date between '{y}-08-01T00:00:00' and '{y}-08-31T23:59:59'"


def q(select, where, group=None, order=None, limit=50000):
    params = {"$select": select, "$where": where, "$limit": limit}
    if group:
        params["$group"] = group
    if order:
        params["$order"] = order
    url = BASE + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "rca-playbook/1.0"})
            return json.loads(urllib.request.urlopen(req, timeout=180).read())
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url}")


def write(name, rows, fields):
    path = OUT / name
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})
    return path


def fetch(fetch_date: str) -> list:
    files = []
    # 1. DEP water and sewer requests by month and label, Aug 2025 - Aug 2026
    rows = q("date_trunc_ym(created_date) as month, complaint_type, count(*) as n",
             f"agency='DEP' AND {LABELS} AND created_date between '2025-08-01T00:00:00' and '2026-08-31T23:59:59'",
             "month, complaint_type", "month")
    files.append(write("dep_labels_monthly.csv", rows, ["month", "complaint_type", "n"]))
    # 2. the same, by day, May - Aug 2026 (to date the label switch)
    rows = q("date_trunc_ymd(created_date) as day, complaint_type, count(*) as n",
             f"agency='DEP' AND {LABELS} AND created_date between '2026-05-01T00:00:00' and '2026-08-31T23:59:59'",
             "day, complaint_type", "day")
    files.append(write("dep_labels_daily.csv", rows, ["day", "complaint_type", "n"]))
    # 3. August requests, all agencies: how many, and how many closed by each cut-off date
    rows = []
    for y in ["2025", "2026"]:
        rows.append({"month": f"{y}-08", "measure": "requests", "n": q("count(*) as n", AUG(y))[0]["n"]})
        for cut in [f"{y}-09-15", "2026-09-15", fetch_date]:
            n = q("count(*) as n", f"{AUG(y)} AND closed_date <= '{cut}T23:59:59'")[0]["n"]
            rows.append({"month": f"{y}-08", "measure": f"closed by {cut}", "n": n})
    files.append(write("august_closure.csv", rows, ["month", "measure", "n"]))
    # 4. HPD (housing) requests by complaint type, August 2025 and August 2026
    rows = []
    for y in ["2025", "2026"]:
        for r in q("complaint_type, count(*) as n", f"agency='HPD' AND {AUG(y)}", "complaint_type", "n DESC"):
            rows.append({"month": f"{y}-08", **r})
    files.append(write("hpd_august_types.csv", rows, ["month", "complaint_type", "n"]))
    return files


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = OUT / "manifest.json"
    if manifest.exists():
        m = json.loads(manifest.read_text())
        for name, h in m["files"].items():
            got = sha256(OUT / name)
            if got != h:
                raise ValueError(f"{name}: checksum {got} differs from the frozen snapshot {h}")
        print(f"ok  NYC 311 snapshot fetched {m['fetched_at']} ({len(m['files'])} files)")
        return
    OUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    files = fetch(now.strftime("%Y-%m-%d"))
    manifest.write_text(json.dumps({"fetched_at": now.strftime("%Y-%m-%d %H:%M UTC"), "source": BASE,
                                    "files": {p.name: sha256(p) for p in files}}, indent=2))
    print(f"fetched and froze {len(files)} files in {OUT}")


if __name__ == "__main__":
    main()
