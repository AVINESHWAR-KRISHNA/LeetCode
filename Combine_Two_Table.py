import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    Output = pd.merge(person, address, how='left', on='personId')
    Output.drop(['personId','addressId'], axis=1, inplace=True)
    # Output = Output[['firstName', 'lastName', 'city', 'state']]

    return Output