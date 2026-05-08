import pandas as pd

def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(
        ["user_id", "action", "action_date"]
    ).copy()

    activity["action_date"] = pd.to_datetime(activity["action_date"])

    activity["rn"] = activity.groupby(
        ["user_id", "action"]
    ).cumcount()

    activity["grp"] = (
        activity["action_date"]
        - pd.to_timedelta(activity["rn"], unit="D")
    )

    streaks = (
        activity.groupby(["user_id", "action", "grp"])
        .agg(
            streak_length=("action_date", "count"),
            start_date=("action_date", "min"),
            end_date=("action_date", "max")
        )
        .reset_index()
    )

    streaks = streaks[streaks["streak_length"] >= 5]

    streaks = (
        streaks.sort_values(
            ["user_id", "streak_length"],
            ascending=[True, False]
        )
        .drop_duplicates("user_id")
    )

    result = streaks[
        ["user_id", "action", "streak_length", "start_date", "end_date"]
    ].sort_values(
        ["streak_length", "user_id"],
        ascending=[False, True]
    )

    return result
