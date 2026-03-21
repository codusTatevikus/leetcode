import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    primary = employee[employee["primary_flag"] == "Y"]

    single = (
        employee.groupby("employee_id")
        .filter(lambda x: len(x) == 1)
    )

    result = pd.concat([primary, single])[["employee_id", "department_id"]]

    return result.reset_index(drop=True)