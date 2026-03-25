from pathlib import Path
import pandas as pd 

RAW_DATA_PATH = Path("data/raw")

FILES = { 
    "customers": "customers.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "products": "products.csv",
    "payments": "payments.csv"
}

def load_csv(file_path: Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame"""
    return pd.read_csv(file_path)

def inspect_dataframe(name: str, df: pd.DataFrame) -> None:
    """Print basic information about a dataframe"""
    print(f"Table: {name}")
    print("-" * 20)
    print(f"Shape: {df.shape}")
    print(f"\nColumns: \n{df.columns.tolist()}")
    print(f"\nDtypes: \n{df.dtypes}")
    print(f"\nMissing values: {df.isnull().sum()}")
    print(f"\nFirst five rows: {df.head()}")
 
def main() -> None:
    for table_name, file_name in FILES.items():
        file_path = RAW_DATA_PATH / file_name

        if not file_path.exists():
            print(f"[Warning] File not found for {table_name}: {file_path}")
            continue

        try:
            df = load_csv(file_path)
            inspect_dataframe(table_name, df)
        except Exception as error:
                print(f"[ERROR] Could not process {table_name} : {error}")

if __name__ == "__main__":
    main()