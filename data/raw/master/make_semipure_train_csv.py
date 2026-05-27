import pandas as pd

KEEP = [
    # identifiers
    "SMILES",
    "Compound ID",
    "Semi-Pure Batch ID",
    # activity measurements
    "Semi-Pure EC50s (µM)",
    "Semi-Pure pEC50s (log)",
    "Semi-Pure Emax normalized",
    "Semi-Pure Emax raw",
    "Corrected Semi-Pure EC50 (µM)",
    "Corrected Semi-Pure pEC50 (log)",
    "Semi-Pure DRC pEC50 SE (log)",
    "Corrected Semi-Pure pEC50 ±1 SE (log)",
    "Semi-Pure pEC50 ±95% CI (log)",
    "Corrected Semi-Pure pEC50 ±95% CI (log)",
    # CAD quantification
    "Volatility",
    "Semi-pure EvapT (°C)",
    "Semi-Pure Theoretical Mass-on-Column (ng)",
    "Semi-Pure Peak Area (pA*min)",
    "Semi-Pure Actual Mass-on-Column (ng)",
    "Semi-Pure Product Yield (%)",
    "Semi-Pure Correction Factor",
    "Semi-Pure CAD Peak Area CV (%)",
    "Semi-Pure CAD Slope CV (%)",
    "Semi-Pure CAD Yield SE (log10)",
]

df = pd.read_csv("pxr-challenge_96-compound-uscale-semi-pure.csv")
df = df[KEEP].rename(columns={"Compound ID": "OCNT_ID"})
df.to_csv("pxr-challenge_96-compound-uscale-semi-pure_TRAIN.csv", index=False)
print(f"Wrote {len(df)} rows, {len(df.columns)} columns.")
