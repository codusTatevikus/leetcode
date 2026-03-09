import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balances = (
        transactions
        .groupby("account", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "balance"})
    )

    result = (
        users
        .merge(balances, on="account", how="left")
        .fillna(0)
    )

    result = result[result["balance"] > 10000][["name", "balance"]]

    return result.reset_index(drop=True)