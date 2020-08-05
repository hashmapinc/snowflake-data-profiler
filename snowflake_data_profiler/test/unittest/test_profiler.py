import pytest
import pandas as pd
import mock
from mock import patch, MagicMock, create_autospec
from snowflake_data_profiler.profiling.profiler import get_snowflake_account_name, establish_connection, create_cursor, get_profile_results

#==============================================================================
# python testing for profiler.py
#==============================================================================


# python testing for establish_connection
def test_establish_connection():

    with pytest.raises(ValueError):
        establish_connection('','','','','','')

    with pytest.raises(ValueError):
        establish_connection(sfUser='user',
                             sfPswd='password',
                             sfURL='',
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='table')

    with pytest.raises(ValueError):
        establish_connection(sfUser=None,
                             sfPswd='password',
                             sfURL='url',
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='table')

    with pytest.raises(ValueError):
        establish_connection(sfUser='user',
                             sfPswd='password',
                             sfURL=None,
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='table',
                             sfRole='role')

    with pytest.raises(ValueError):
        establish_connection(sfUser='user',
                             sfPswd='password',
                             sfURL='url',
                             sfDatabase='database',
                             sfSchema='schema',
                             sfTable='',
                             sfRole='role')

    with mock.patch('snowflake_data_profiler.profiling.profiler.connector.connect', return_value='some connection value') as mock_connect:
        assert establish_connection(sfUser='user', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole=None) == 'some connection value'

        mock_connect.assert_called_with(user='user', password='password', account='url', database='database', schema='schema', role=None)

    with mock.patch('snowflake_data_profiler.profiling.profiler.connector.connect', return_value=['a', 'nice', 'fancy', 'list']) as mock_connect:
        assert establish_connection(sfUser='user', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole='role') == ['a', 'nice', 'fancy', 'list']

        mock_connect.assert_called_with(user='user', password='password', account='url', database='database', schema='schema', role='role')


def test_create_cursor():
    mock_create_cursor = create_autospec(create_cursor, return_value='some pd_df')
    assert mock_create_cursor(con='connector', sfDatabase='database', sfSchema='schema', sfTable='table', sfWarehouse='warehouse') == 'some pd_df'

    with pytest.raises(ValueError):
        create_cursor(con='connector', sfDatabase='database', sfSchema='schema', sfTable=None, sfWarehouse='warehouse')

    with pytest.raises(ValueError):
        create_cursor(con='', sfDatabase='database', sfSchema='schema', sfTable='table', sfWarehouse='warehouse')



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


# python testing for get_profile_results
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

















