import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders["customer_number"].value_counts()
    max_count = counts.max()
    
    result = counts[counts == max_count].index.to_frame(index=False, name="customer_number")
    
    return result
