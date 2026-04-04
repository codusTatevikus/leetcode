import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    result = queue.sort_values("turn").copy()
    result["total_weight"] = result["weight"].cumsum()
    result = result[result["total_weight"] <= 1000].tail(1)[["person_name"]]

    return result.reset_index(drop=True)