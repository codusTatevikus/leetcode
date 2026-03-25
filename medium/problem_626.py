import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat = seat.copy()

    n = len(seat)

    seat["new_id"] = seat["id"]

    seat.loc[seat["id"] % 2 == 1, "new_id"] = seat["id"] + 1
    seat.loc[seat["id"] % 2 == 0, "new_id"] = seat["id"] - 1

    if n % 2 == 1:
        seat.loc[seat["id"] == n, "new_id"] = n

    result = seat.sort_values("new_id")[["id", "student"]]
    result["id"] = range(1, n + 1)

    return result