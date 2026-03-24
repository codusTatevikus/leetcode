import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = (
        person.groupby("email")
        .size()
        .reset_index(name="cnt")
    )

    result = result[result["cnt"] > 1][["email"]]
    result = result.rename(columns={"email": "Email"})

    return result.reset_index(drop=True)