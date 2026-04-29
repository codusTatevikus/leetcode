import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    result = scores.copy()
    result["rank"] = result["score"].rank(method="dense", ascending=False).astype(int)
    return result.sort_values("score", ascending=False)[["score", "rank"]]
