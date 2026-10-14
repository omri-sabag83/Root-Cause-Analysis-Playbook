"""Copy the source files the "reuse" modules need into data/raw/ and verify them.

Usage (from the project root): python data/get_data.py

Some modules re-run an earlier investigation from the author's private analysis
workspace. Those source files are take-home-exercise data whose licence does not
clearly allow redistribution, so they are NOT in this repo (data/raw/ is gitignored).
The notebooks keep their outputs, so every number can still be read without them.

Source folder: $RCA_SOURCE_DIR, default ~/Documents/Python_Projects/AI Analyst Workspace/Data
Each file is checked against a fixed SHA-256 checksum, so a changed file fails loudly.
"""
import hashlib
import os
import shutil
from pathlib import Path

RAW = Path(__file__).resolve().parent / "raw"
SOURCE = Path(os.environ.get(
    "RCA_SOURCE_DIR",
    Path.home() / "Documents" / "Python_Projects" / "AI Analyst Workspace" / "Data"))

# file name -> SHA-256. Modules add their files here as they are built.
FILES = {
    "E01_Flare_Assignment_Data.xlsx": "1fff15683398a6c3d5921be756fc941f3e4783540f438e2354684acb985cd5fb",
    "E04_AlignedUp_Assignment_Data.csv": "c5bfd03b06eaa57d748c836dea42a9becf5327b4d3f89cbb49f80ed6ab8d828e",
    "E08_Ravenstack_Data/ravenstack_accounts.csv": "348d8ba906b7776894b5236b2e7aa91a503d41670dbc9aad30c37b503c9abef5",
    "E08_Ravenstack_Data/ravenstack_churn_events.csv": "6391c41d8291b7b4845ec9a84d3837c2ed230a33a32a854ec33d4e66dc150940",
    "E08_Ravenstack_Data/ravenstack_feature_usage.csv": "c081da2be8caf987d07f0f79ceb0619aba523d819529230ed6df77984fa21d4e",
    "E08_Ravenstack_Data/ravenstack_subscriptions.csv": "dcf1d93ca9a35e0dcba0ab686d255f0e9ec26512970bbf0944cf19cbef2d751a",
    "E08_Ravenstack_Data/ravenstack_support_tickets.csv": "ba0006951479771ee9f93c98789c96bc5fec892cf11f867afb28194f0b76d220",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    RAW.mkdir(exist_ok=True)
    for name, expected in FILES.items():
        target = RAW / name
        target.parent.mkdir(exist_ok=True)
        if not target.exists():
            src = SOURCE / name
            if not src.exists():
                raise FileNotFoundError(f"{src} not found. Set RCA_SOURCE_DIR to the folder holding it.")
            shutil.copy2(src, target)
        got = sha256(target)
        if got != expected:
            raise ValueError(f"{name}: checksum {got} does not match the expected {expected}")
        print(f"ok  {name}")


if __name__ == "__main__":
    main()
