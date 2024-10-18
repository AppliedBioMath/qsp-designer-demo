"""
An example module to demonstrate how to write reusable utility functions for project work.

Functions
---------
utility_example
    Sample utility function that prints "hello".

"""

import pandas as pd

def vpop_to_param(path: str) -> pd.DataFrame:
    vpop = pd.read_csv(path)
    return df_to_param(vpop)  

def df_to_param(vpop: pd.DataFrame) -> pd.DataFrame:
    assert 'ID' in vpop.keys(), "VPop must contain ID column"
    params = pd.melt(
        vpop, 
        id_vars=['ID'], 
        value_vars=vpop.drop('ID', axis=1).keys().tolist(), # Gets parameter names, ignoring ID
        var_name = 'parameter'
    ).sort_values('ID').reset_index(drop=True)
    params['unit'] = 1
    return params 