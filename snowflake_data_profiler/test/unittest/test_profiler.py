import pytest
from snowflake_data_profiler.profiling.profiler import get_snowflake_account_name, connect_to_snowflake, get_profile_results

#==============================================================================
# python testing for profiler.py
#==============================================================================


# python testing for connect_to_snowflake
def test_connect_to_snowflake():

    with pytest.raises(ValueError):
        connect_to_snowflake('','','','','','')


# python testing for get_snowflake_account_name
def test_get_snowflake_account_name():

    result = get_snowflake_account_name('hashmap')
    assert result == 'hashmap'

    result = get_snowflake_account_name('hashmap.snowflakecomputing.com')
    assert result == 'hashmap'

    result = get_snowflake_account_name('https://hashmap.snowflakecomputing.com')
    assert result == 'hashmap'


def test_get_profile_results():

    with pytest.raises(TypeError):
        get_profile_results([10, 8, 5353, 1414])

    with pytest.raises(TypeError):
        get_profile_results({'a':[10, 8, 5353, 1414], 'b':'ahfjahjhafa'})

    with pytest.raises(ValueError):
        get_profile_results('')





