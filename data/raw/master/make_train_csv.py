import pandas as pd

KEEP = [
    # identifiers
    "SMILES",
    "Compound ID",
    "Crude Batch ID",
    # activity measurements
    "Crude EC50s (µM)",
    "Crude pEC50s (log)",
    "Crude Emax normalized",
    "Crude Emax raw",
    "Corrected Crude EC50 (µM)",
    "Corrected Crude pEC50 (log)",
    "Crude DRC pEC50 SE (log)",
    "Corrected Crude pEC50 ±1 SE (log)",
    "Crude pEC50 ±95% CI (log)",
    "Corrected Crude pEC50 ±95% CI (log)",
    # CAD quantification
    "Volatility",
    "CAD Yield/Volatility Note",
    "Crude EvapT (°C)",
    "Crude Theoretical Mass-on-Column (ng)",
    "Crude Peak Area (pA*min)",
    "Crude Actual Mass-on-Column (ng)",
    "Crude Product Yield (%)",
    "Crude Correction Factor",
    "Crude CAD Peak Area CV (%)",
    "Crude CAD Slope CV (%)",
    "Crude CAD Yield SE (log10)",
]

df = pd.read_csv("pxr-challenge_htchem-libraries.csv")
df = df[KEEP].rename(columns={"Compound ID": "OCNT_ID"})
df.to_csv("pxr-challenge_htchem-libraries_TRAIN.csv", index=False)
print(f"Wrote {len(df)} rows, {len(df.columns)} columns.")
