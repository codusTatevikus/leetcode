import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks["value"] = stocks.apply(
        lambda x: -x["price"] if x["operation"] == "Buy" else x["price"],
        axis=1
    )

    result = (
        stocks.groupby("stock_name", as_index=False)["value"]
        .sum()
        .rename(columns={"value": "capital_gain_loss"})
    )

    return result