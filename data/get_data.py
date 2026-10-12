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
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    RAW.mkdir(exist_ok=True)
    for name, expected in FILES.items():
        target = RAW / name
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
