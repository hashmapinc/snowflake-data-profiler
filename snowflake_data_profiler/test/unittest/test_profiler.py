import pytest
import pandas as pd
from snowflake_data_profiler.profiling.profiler import get_snowflake_account_name, connect_to_snowflake, get_profile_results

#==============================================================================
# python testing for profiler.py
#==============================================================================


# python testing error handling for connect_to_snowflake
def test_connect_to_snowflake():

    with pytest.raises(ValueError):
        connect_to_snowflake('','','','','','')

    with pytest.raises(ValueError):
        connect_to_snowflake(sfUser='user',
                             sfPswd='password',
                             sfURL='',
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='table')

    with pytest.raises(ValueError):
        connect_to_snowflake(sfUser=None,
                             sfPswd='password',
                             sfURL='url',
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='table')

    with pytest.raises(ValueError):
        connect_to_snowflake(sfUser='user',
                             sfPswd='password',
                             sfURL=None,
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='table',
                             sfWarehouse=None,
                             sfRole='role')

    with pytest.raises(ValueError):
        connect_to_snowflake(sfUser='user',
                             sfPswd='password',
                             sfURL='url',
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='',
                             sfWarehouse='warehouse',
                             sfRole='role')


# python testing for get_snowflake_account_name
def test_get_snowflake_account_name():

    result = get_snowflake_account_name('hashmap')
    assert result == 'hashmap'

    result = get_snowflake_account_name('hashmap.snowflakecomputing.com')
    assert result == 'hashmap'

    result = get_snowflake_account_name('https://hashmap.snowflakecomputing.com')
    assert result == 'hashmap'

    result = get_snowflake_account_name('https://hashmap.fake.com')
    assert result == 'https://hashmap.fake.com'

    result = get_snowflake_account_name('https://hashmap.fake.snowflakecomputing.com.fake.com')
    assert result == 'hashmap.fake'


# python testing error handling for get_profile_results
def test_get_profile_results():

    with pytest.raises(TypeError):
        get_profile_results({'a': 10, 'b':9})

    with pytest.raises(TypeError):
        get_profile_results(10)

    with pytest.raises(TypeError):
        get_profile_results([1,2,3,3,4,5,5])

    with pytest.raises(TypeError):
        get_profile_results('This is a dataframe. I promise.')

    d = {'col1': [1, 2], 'col2': [3, 4]}
    result = get_profile_results(pd.DataFrame(data=d))
    assert type(result) == str

















