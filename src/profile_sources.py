from pathlib import Path
import pandas as pd

RAW = Path("data/raw")

customers = pd.read_csv(RAW / "customers.csv")
orders = pd.read_json(RAW / "orders.json")
products = pd.read_parquet(RAW / "products.parquet")

datasets = {
    "customers.csv": customers,
    "orders.json": orders,
    "products.parquet": products,
}

for name, df in datasets.items():
    print(f"\n=== {name} ===")
    print("file size (KB):", round((RAW / name).stat().st_size / 1024, 2))
    print("shape:", df.shape)
    print("rows:", len(df))
    print("columns:", list(df.columns))
    print("dtypes:\n", df.dtypes)
    print("nulls:\n", df.isna().sum())
    df_date = df.drop(columns=["shipping"], errors="ignore")
    print("duplicate rows:", df_date.duplicated().sum())
    print("unique values per column:\n", df_date.nunique())
    print("minimum values per column:\n", df.min(numeric_only=True))
    print("maximum values per column:\n", df.max(numeric_only=True))
    print(df.head())
    if "order_timestamp" in df.columns:
        parsed_timestamps = pd.to_datetime(df["order_timestamp"], errors="coerce")
        print("earliest order_timestamp:", parsed_timestamps.min())
        print("latest order_timestamp:", parsed_timestamps.max())

    if "signup_date" in df.columns:
        parsed_dates = pd.to_datetime(df["signup_date"], errors="coerce")
        print("earliest signup_date:", parsed_dates.min())
        print("latest signup_date:", parsed_dates.max())