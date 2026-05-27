"""Convert each sheet of the PXR master Excel file to a CSV.

Naming convention follows the HuggingFace dataset openadmet/pxr-challenge-train-test:
  pxr-challenge_<sheet-slug>.csv  (lowercase, spaces→hyphens, special chars stripped)
"""

import re
import sys
from pathlib import Path

import pandas as pd


EXCEL_FILE = Path("PXR_CAD_Blog_Post_Master_Raw_Data.xlsx")
PREFIX = "pxr-challenge_"

# µ (micro sign U+00B5 and Greek mu U+03BC) → "u"
_SPECIAL = str.maketrans({"µ": "u", "μ": "u", "°": "deg"})


def sheet_name_to_slug(name: str) -> str:
    name = name.translate(_SPECIAL)
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return name.strip("-")


def main(excel_path: Path = EXCEL_FILE, out_dir: Path | None = None) -> None:
    if out_dir is None:
        out_dir = excel_path.parent

    xl = pd.ExcelFile(excel_path, engine="openpyxl")
    print(f"Found {len(xl.sheet_names)} sheet(s) in {excel_path.name}")

    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        slug = sheet_name_to_slug(sheet)
        out_path = out_dir / f"{PREFIX}{slug}.csv"
        df.to_csv(out_path, index=False)
        print(f"  {sheet!r:45s} -> {out_path.name}  ({len(df)} rows, {len(df.columns)} cols)")

    xl.close()


if __name__ == "__main__":
    excel = Path(sys.argv[1]) if len(sys.argv) > 1 else EXCEL_FILE
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    main(excel, out)
