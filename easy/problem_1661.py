import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    pivoted = activity.pivot(
        index=["machine_id", "process_id"],
        columns="activity_type",
        values="timestamp"
    ).reset_index()

    pivoted["processing_time"] = pivoted["end"] - pivoted["start"]

    result = (
        pivoted.groupby("machine_id", as_index=False)["processing_time"]
        .mean()
    )

    result["processing_time"] = result["processing_time"].round(3)

    return result