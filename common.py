"""Shared loaders, chart settings and table printing for every module.

load_e01()  the E01 funnel data (one row per lead), as used in Modules 1 and 11
show()      print a table with text columns left-aligned, numbers right-aligned
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"

# Chart palette: reference categorical slots (same as the earlier playbooks).
BLUE, ORANGE, AQUA, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#888888"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.alpha": 0.25, "figure.dpi": 110})

# Every chart image gets a thin black frame (shared with the other repos: chart_style.py).
import chart_style  # noqa: E402,F401

# E01 funnel: each step is a date column; blank = step not reached.
E01_STEPS = {
    "onboarding_start_date": "Started Onboarding",
    "lead_form_submitted": "Lead Form",
    "free_consultation_call_date": "Free Consultation",
    "strategy_session_call_date": "Strategy Session",
    "sales_call_date": "Sales Call",
    "closed_won_date": "Closed Won",
}


def _need(name: str) -> Path:
    path = RAW / name
    if not path.exists():
        raise FileNotFoundError(f"{path} missing: run `python data/get_data.py` first (see its docstring).")
    return path


def load_e01() -> pd.DataFrame:
    """E01 'Main Funnel Data' sheet: step dates parsed (day first), plus ob_day = onboarding date."""
    df = pd.read_excel(_need("E01_Flare_Assignment_Data.xlsx"), sheet_name="Main Funnel Data")
    for col in E01_STEPS:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors="coerce")
    df["ob_day"] = df["onboarding_start_date"].dt.strftime("%Y-%m-%d")
    return df


def load_e01_reference() -> pd.DataFrame:
    """E01 'Funnel table' sheet, first block: share of each day's starters reaching each step."""
    ref = pd.read_excel(_need("E01_Flare_Assignment_Data.xlsx"), sheet_name="Funnel table", header=None)
    first = ref.index[ref[0].astype(str).str.strip() == "onboarding_start_date"][0]
    block = ref.iloc[first + 1: first + 7].copy()
    block.columns = ["ob_day", "users"] + list(E01_STEPS)[1:]
    block["ob_day"] = pd.to_datetime(block["ob_day"], dayfirst=True).dt.strftime("%Y-%m-%d")
    for col in block.columns[1:]:
        block[col] = pd.to_numeric(block[col])
    return block.reset_index(drop=True)


def show(df: pd.DataFrame, index: bool = False) -> None:
    """Print a table with text columns left-aligned and numeric columns right-aligned."""
    import re
    if index:
        df = df.reset_index()
    numeric = re.compile(r"^[-+−]?[\d,]*\.?\d+%?$")
    cols = [str(c) for c in df.columns]
    cells = [[str(v) for v in df[c]] for c in df.columns]
    blank = {"n/a", "no data", "—", ""}
    is_text = [not all(numeric.match(v) or v in blank for v in col) or all(v in blank for v in col) for col in cells]
    widths = [max([len(h)] + [len(v) for v in col]) for h, col in zip(cols, cells)]
    pad = lambda s, w, left: s.ljust(w) if left else s.rjust(w)
    print("  ".join(pad(h, w, t) for h, w, t in zip(cols, widths, is_text)).rstrip())
    for r in range(len(df)):
        print("  ".join(pad(col[r], w, t) for col, w, t in zip(cells, widths, is_text)).rstrip())
