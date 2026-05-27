#!/usr/bin/env python3
"""Generate Figure 6 CAD-correction validation panels.

The master workbook stores several Figure 6 columns as Excel formulas. This
script recomputes the plotted pEC50, CAD-yield, correction, and confidence
interval values directly from the raw workbook columns so it can run from a
fresh clone without requiring Excel formula recalculation.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "octant-pxr-figure-6"

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
MASTER_WORKBOOK = REPO_ROOT / "data" / "raw" / "master" / "PXR_CAD_Blog_Post_Master_Raw_Data.xlsx"
OUTPUT_DIR = REPO_ROOT / "figures" / "static" / "figure-6-python"
SHEET_NAME = "Crude-SP to Pure Correlation"

PURE_EXPERIMENTS = ("OPA_PXR-032", "OPA_PXR-035", "OPA_PXR-036")
LOG10_TWO_FOLD = math.log10(2)


@dataclass(frozen=True)
class PanelSpec:
    key: str
    title: str
    x_col: str
    y_col: str
    color_col: str
    xerr_col: str
    yerr_col: str
    x_label: str
    y_label: str
    output_stem: str


PANEL_SPECS = (
    PanelSpec(
        key="6a",
        title="Uncorrected Crude vs Pure (95% CI)",
        x_col="Pure pEC50s (log)",
        y_col="Crude pEC50s (log)",
        color_col="Crude Product Yield (%)",
        xerr_col="Pure pEC50 ±95% CI (log)",
        yerr_col="Crude pEC50 ±95% CI (log)",
        x_label="Pure pEC50",
        y_label="Uncorrected Crude pEC50",
        output_stem="figure-6a-uncorrected-crude-vs-pure-95ci",
    ),
    PanelSpec(
        key="6b",
        title="Corrected Crude vs Pure (95% CI)",
        x_col="Pure pEC50s (log)",
        y_col="Corrected Crude pEC50 (log)",
        color_col="Crude Product Yield (%)",
        xerr_col="Pure pEC50 ±95% CI (log)",
        yerr_col="Corrected Crude pEC50 ±95% CI (log)",
        x_label="Pure pEC50",
        y_label="Corrected Crude pEC50",
        output_stem="figure-6b-corrected-crude-vs-pure-95ci",
    ),
    PanelSpec(
        key="6c",
        title="Corrected Crude vs Corrected Semi-Pure (95% CI)",
        x_col="Corrected Semi-Pure pEC50 (log)",
        y_col="Corrected Crude pEC50 (log)",
        color_col="Avg CAD Yield (%)",
        xerr_col="Corrected Semi-Pure pEC50 ±95% CI (log)",
        yerr_col="Corrected Crude pEC50 ±95% CI (log)",
        x_label="Corrected Semi-Pure pEC50",
        y_label="Corrected Crude pEC50",
        output_stem="figure-6c-corrected-crude-vs-corrected-semipure-95ci",
    ),
)


def numeric(series: pd.Series) -> pd.Series:
    cleaned = series.astype("string").str.strip()
    cleaned = cleaned.replace({"no data": pd.NA, "-": pd.NA, "": pd.NA})
    return pd.to_numeric(cleaned, errors="coerce")


def pec50_from_ec50_um(values: pd.Series) -> pd.Series:
    values = numeric(values)
    output = pd.Series(np.nan, index=values.index, dtype=float)
    mask = values.gt(0)
    output.loc[mask] = 6 - np.log10(values.loc[mask])
    return output


def product_yield_percent(peak_area: pd.Series, theoretical_mass_ng: pd.Series) -> pd.Series:
    peak_area = numeric(peak_area)
    theoretical_mass_ng = numeric(theoretical_mass_ng)
    output = pd.Series(np.nan, index=peak_area.index, dtype=float)
    mask = peak_area.notna() & theoretical_mass_ng.gt(0)
    output.loc[mask] = 12.5 * peak_area.loc[mask] / theoretical_mass_ng.loc[mask] * 100
    return output


def corrected_pec50(ec50_um: pd.Series, yield_percent: pd.Series) -> pd.Series:
    ec50_um = numeric(ec50_um)
    yield_percent = numeric(yield_percent)
    corrected_ec50 = ec50_um * (yield_percent / 100)
    return pec50_from_ec50_um(corrected_ec50)


def root_sum_square_mean(values: pd.DataFrame) -> pd.Series:
    numeric_values = values.apply(numeric)
    counts = numeric_values.notna().sum(axis=1)
    sumsq = (numeric_values.fillna(0) ** 2).sum(axis=1)
    output = pd.Series(np.nan, index=values.index, dtype=float)
    mask = counts.gt(0)
    output.loc[mask] = np.sqrt(sumsq.loc[mask]) / counts.loc[mask]
    return output


def cad_yield_se_log10(peak_area: pd.Series) -> pd.Series:
    peak_area = numeric(peak_area)
    output = pd.Series(np.nan, index=peak_area.index, dtype=float)
    mask = peak_area.gt(0)
    peak_area_cv = 43.15 / peak_area.loc[mask] + 0.86
    slope_cv = 31.74
    output.loc[mask] = np.sqrt((peak_area_cv / 100) ** 2 + (slope_cv / 100) ** 2) / np.log(10)
    return output


def corrected_pec50_se(drc_se: pd.Series, yield_se_log10: pd.Series) -> pd.Series:
    drc_se = numeric(drc_se)
    yield_se_log10 = numeric(yield_se_log10)
    output = pd.Series(np.nan, index=drc_se.index, dtype=float)
    mask = drc_se.notna() & yield_se_log10.notna()
    output.loc[mask] = np.sqrt(drc_se.loc[mask] ** 2 + yield_se_log10.loc[mask] ** 2)
    return output


def load_and_calculate(master_workbook: Path) -> pd.DataFrame:
    df = pd.read_excel(master_workbook, sheet_name=SHEET_NAME, engine="openpyxl")

    for experiment in PURE_EXPERIMENTS:
        df[f"{experiment} pEC50 (log)"] = pec50_from_ec50_um(df[f"{experiment} (µM)"])

    pure_pec50_cols = [f"{experiment} pEC50 (log)" for experiment in PURE_EXPERIMENTS]
    pure_se_cols = [f"{experiment} pEC50 SE (log)" for experiment in PURE_EXPERIMENTS]
    df["Pure pEC50s (log)"] = df[pure_pec50_cols].mean(axis=1, skipna=True)
    df["Pure pEC50 ±1 SE (log)"] = root_sum_square_mean(df[pure_se_cols])

    df["Crude Product Yield (%)"] = product_yield_percent(
        df["Crude Peak Area (pA*min)"],
        df["Crude Theoretical Mass-on-Column (ng)"],
    )
    df["Semi-Pure Product Yield (%)"] = product_yield_percent(
        df["Semi-Pure Peak Area (pA*min)"],
        df["Semi-Pure Theoretical Mass-on-Column (ng)"],
    )
    df["Avg CAD Yield (%)"] = (df["Crude Product Yield (%)"] + df["Semi-Pure Product Yield (%)"]) / 2

    df["Crude pEC50s (log)"] = pec50_from_ec50_um(df["Crude EC50s (µM)"])
    df["Semi-Pure pEC50s (log)"] = pec50_from_ec50_um(df["Semi-Pure EC50s (µM)"])
    df["Corrected Crude pEC50 (log)"] = corrected_pec50(df["Crude EC50s (µM)"], df["Crude Product Yield (%)"])
    df["Corrected Semi-Pure pEC50 (log)"] = corrected_pec50(
        df["Semi-Pure EC50s (µM)"],
        df["Semi-Pure Product Yield (%)"],
    )

    crude_yield_se = cad_yield_se_log10(df["Crude Peak Area (pA*min)"])
    semipure_yield_se = cad_yield_se_log10(df["Semi-Pure Peak Area (pA*min)"])
    df["Corrected Crude pEC50 ±1 SE (log)"] = corrected_pec50_se(df["Crude DRC pEC50 SE (log)"], crude_yield_se)
    df["Corrected Semi-Pure pEC50 ±1 SE (log)"] = corrected_pec50_se(
        df["Semi-Pure DRC pEC50 SE (log)"],
        semipure_yield_se,
    )

    ci_cols = {
        "Pure pEC50 ±95% CI (log)": "Pure pEC50 ±1 SE (log)",
        "Crude pEC50 ±95% CI (log)": "Crude DRC pEC50 SE (log)",
        "Semi-Pure pEC50 ±95% CI (log)": "Semi-Pure DRC pEC50 SE (log)",
        "Corrected Crude pEC50 ±95% CI (log)": "Corrected Crude pEC50 ±1 SE (log)",
        "Corrected Semi-Pure pEC50 ±95% CI (log)": "Corrected Semi-Pure pEC50 ±1 SE (log)",
    }
    for ci_col, se_col in ci_cols.items():
        df[ci_col] = numeric(df[se_col]) * 1.96

    return df


def common_axis_limits(df: pd.DataFrame) -> tuple[float, float]:
    columns = [
        "Pure pEC50s (log)",
        "Crude pEC50s (log)",
        "Corrected Crude pEC50 (log)",
        "Corrected Semi-Pure pEC50 (log)",
    ]
    values = pd.concat([numeric(df[col]) for col in columns], ignore_index=True).dropna()
    if values.empty:
        raise ValueError("No finite pEC50 values found for Figure 6")
    lower = math.floor((values.min() - 0.35) * 2) / 2
    upper = math.ceil((values.max() + 0.35) * 2) / 2
    return lower, upper


def add_reference_lines_and_limits(ax: plt.Axes, limits: tuple[float, float]) -> None:
    lower, upper = limits
    ax.plot([lower, upper], [lower, upper], color="#b73737", linestyle="--", linewidth=1.6, label="1:1")
    ax.plot(
        [lower, upper],
        [lower + LOG10_TWO_FOLD, upper + LOG10_TWO_FOLD],
        color="#333333",
        linestyle=":",
        linewidth=1.2,
        alpha=0.65,
        label="2-fold",
    )
    ax.plot(
        [lower, upper],
        [lower - LOG10_TWO_FOLD, upper - LOG10_TWO_FOLD],
        color="#333333",
        linestyle=":",
        linewidth=1.2,
        alpha=0.65,
    )
    ax.set_xlim(lower, upper)
    ax.set_ylim(lower, upper)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.45)


def panel_data(df: pd.DataFrame, spec: PanelSpec) -> pd.DataFrame:
    needed = [spec.x_col, spec.y_col, spec.color_col, spec.xerr_col, spec.yerr_col]
    data = df.copy()
    for col in needed:
        data[col] = numeric(data[col])
    return data.dropna(subset=[spec.x_col, spec.y_col, spec.color_col]).copy()


def strip_trailing_whitespace(path: Path) -> None:
    lines = path.read_text().splitlines()
    path.write_text("\n".join(line.rstrip() for line in lines) + "\n")


def draw_panel(df: pd.DataFrame, spec: PanelSpec, limits: tuple[float, float], output_dir: Path, formats: Iterable[str]) -> dict[str, float]:
    data = panel_data(df, spec)
    if data.empty:
        raise ValueError(f"No rows available for {spec.title}")

    mae = float(np.mean(np.abs(data[spec.y_col] - data[spec.x_col])))

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.errorbar(
        data[spec.x_col],
        data[spec.y_col],
        xerr=data[spec.xerr_col],
        yerr=data[spec.yerr_col],
        fmt="none",
        ecolor="#333333",
        alpha=0.7,
        zorder=1,
        elinewidth=1,
    )
    scatter = ax.scatter(
        data[spec.x_col],
        data[spec.y_col],
        c=data[spec.color_col].clip(lower=0, upper=100),
        cmap="viridis",
        vmin=0,
        vmax=100,
        edgecolor="black",
        linewidths=0.5,
        s=50,
        zorder=2,
    )
    colorbar = fig.colorbar(scatter, ax=ax)
    colorbar.set_label("CAD Yield", fontsize=13)
    colorbar.outline.set_visible(True)
    colorbar.outline.set_color("#333333")

    ax.set_xlabel(spec.x_label)
    ax.set_ylabel(spec.y_label)
    ax.set_title(spec.title, pad=15)
    add_reference_lines_and_limits(ax, limits)
    ax.text(
        0.05,
        0.95,
        f"MAE = {mae:.3f}",
        transform=ax.transAxes,
        fontsize=13,
        verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="#cccccc", alpha=0.9),
    )

    fig.tight_layout()
    output_dir.mkdir(parents=True, exist_ok=True)
    for fmt in formats:
        output_path = output_dir / f"{spec.output_stem}.{fmt}"
        metadata = {"Date": None} if fmt == "svg" else None
        fig.savefig(output_path, dpi=300, bbox_inches="tight", metadata=metadata)
        if fmt == "svg":
            strip_trailing_whitespace(output_path)
    plt.close(fig)

    return {"n": float(len(data)), "mae": mae}


def build_figure_6(master_workbook: Path, output_dir: Path, formats: Iterable[str]) -> pd.DataFrame:
    df = load_and_calculate(master_workbook)
    limits = common_axis_limits(df)
    rows = []
    for spec in PANEL_SPECS:
        stats = draw_panel(df, spec, limits, output_dir, formats)
        rows.append(
            {
                "panel": spec.key,
                "title": spec.title,
                "n": int(stats["n"]),
                "mae": round(stats["mae"], 6),
            }
        )
    summary = pd.DataFrame(rows)
    summary.to_csv(output_dir / "figure-6-panel-summary.csv", index=False)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--master-workbook", type=Path, default=MASTER_WORKBOOK)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--formats", nargs="+", default=["png", "svg"], choices=["png", "svg", "pdf"])
    args = parser.parse_args()

    summary = build_figure_6(args.master_workbook, args.output_dir, args.formats)
    print(f"Figure 6 panels written to: {args.output_dir}")
    print(summary.to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
