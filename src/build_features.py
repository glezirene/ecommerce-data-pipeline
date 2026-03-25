from pathlib import Path 
import pandas as pd 

RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")

PROCESSED_DATA_PATH.mkdir(parents = True, exist_ok = True)

def load_data():

    customers = pd.read_csv(RAW_DATA_PATH / "customers.csv")
    orders =  pd.read_csv(RAW_DATA_PATH / "orders.csv")
    order_items =  pd.read_csv(RAW_DATA_PATH / "order_items.csv")

    return customers, orders, order_items


def build_fact_order_items(orders, order_items):
    # convert date
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    # selection of key information: 'who' bought 'what' and 'when'
    order_subset = orders[["order_id", "customer_id", "order_purchase_timestamp"]]
    # join them
    fct = order_items.merge(
        order_subset,
        # order_items.order_id == orders_subset.order_id
        on = "order_id",
        how = "left")
    # rename for clarity
    fct = fct.rename(
        columns = {"order_purchase_timestamp" : "order_date"}
    )

    return fct

def main(): 
    customers, orders, order_items = load_data()

    fct = build_fact_order_items(orders, order_items)

    print(f"\nFCT Order Items: \n{fct.head()}")
    print("\nShape:", fct.shape)

    fct.to_csv(PROCESSED_DATA_PATH / "fct_order_items.csv", index = False)




if __name__ == "__main__":
    main()


