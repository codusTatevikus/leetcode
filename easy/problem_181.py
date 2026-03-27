import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        employee,
        left_on="managerId",
        right_on="id",
        suffixes=("", "_manager")
    )

    result = merged[merged["salary"] > merged["salary_manager"]][["name"]]
    result = result.rename(columns={"name": "Employee"})

    return result.reset_index(drop=True)