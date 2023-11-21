import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    df_self_join = employee.merge(employee[['id', 'salary']], left_on='managerId', right_on='id', suffixes=('','_manager'))

    filter_df = df_self_join[df_self_join['salary'] > df_self_join['salary_manager']]
    
    result = filter_df[['name']].rename(columns={'name': 'Employee'})

    return result