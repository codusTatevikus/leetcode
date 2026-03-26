import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    result = (
        employees.merge(salaries, on="employee_id", how="outer")
    )

    result = result[
        result["name"].isna() | result["salary"].isna()
    ][["employee_id"]]

    return result.sort_values("employee_id").reset_index(drop=True)