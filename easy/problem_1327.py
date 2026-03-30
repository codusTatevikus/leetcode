import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    feb_orders = orders[
        (orders["order_date"].dt.year == 2020) &
        (orders["order_date"].dt.month == 2)
    ]

    grouped = (
        feb_orders
        .groupby("product_id", as_index=False)["unit"]
        .sum()
    )

    grouped = grouped[grouped["unit"] >= 100]

    result = grouped.merge(products, on="product_id")[["product_name", "unit"]]

    return result