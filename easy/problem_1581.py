import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    result = (
        visits.merge(transactions, on="visit_id", how="left")
    )

    result = result[result["transaction_id"].isna()]

    result = (
        result.groupby("customer_id")
        .size()
        .reset_index(name="count_no_trans")
    )

    return result