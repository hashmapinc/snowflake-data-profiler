import pytest
import pandas as pd
import mock
from mock import create_autospec
from snowflake_data_profiler.profiling.profiler import get_snowflake_account_name, get_snowflake_connection, get_pandas_dataframe, get_profile_results, get_profile


#==============================================================================
# python testing for profiler.py
#==============================================================================


def test_get_profile():
    """Unit testing for get_profile"""

    mock_get_profile = create_autospec(get_profile, return_value='some profile report')
    assert mock_get_profile(sfUser='username', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole='role', sfWarehouse='warehouse') == 'some profile report'
    mock_get_profile.assert_called_with(sfUser='username', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole='role', sfWarehouse='warehouse')

    mock_get_profile = create_autospec(get_profile, return_value='some profile report')
    assert mock_get_profile(sfUser='username', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole=None, sfWarehouse=None) == 'some profile report'
    mock_get_profile.assert_called_with(sfUser='username', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole=None, sfWarehouse=None)

    with pytest.raises(ValueError):
        get_profile(sfUser='username', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable=None, sfRole=None, sfWarehouse=None)

    with pytest.raises(ValueError):
        get_profile(sfUser=None, sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole=None, sfWarehouse=None)

    with pytest.raises(ValueError):
        get_profile(sfUser='username', sfPswd=None, sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole=None, sfWarehouse=None)


def test_get_snowflake_connection():
    """Unit testing for get_snowflake_connection"""

    with pytest.raises(ValueError):
        get_snowflake_connection('','','','','','')

    with pytest.raises(ValueError):
        get_snowflake_connection(sfUser='user',
                                 sfPswd='password',
                                 sfURL='',
                                 sfDatabase='database',
                                 sfSchema='schema',
                                 sfTable='table')

    with pytest.raises(ValueError):
        get_snowflake_connection(sfUser=None,
                                 sfPswd='password',
                                 sfURL='url',
                                 sfDatabase='database',
                                 sfSchema='schema',
                                 sfTable='table')

    with pytest.raises(ValueError):
        get_snowflake_connection(sfUser='user',
                                 sfPswd='password',
                                 sfURL=None,
                                 sfDatabase='database',
                                 sfSchema='schema',
                                 sfTable='table',
                                 sfRole='role')

    with pytest.raises(ValueError):
        get_snowflake_connection(sfUser='user',
                                 sfPswd='password',
                                 sfURL='url',
                                 sfDatabase='database',
                                 sfSchema='schema',
                                 sfTable='',
                                 sfRole='role')

    with mock.patch('snowflake_data_profiler.profiling.profiler.connector.connect', return_value='some connection value') as mock_connect:
        assert get_snowflake_connection(sfUser='user', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole=None) == 'some connection value'

        mock_connect.assert_called_with(user='user', password='password', account='url', database='database', schema='schema', role=None)

    with mock.patch('snowflake_data_profiler.profiling.profiler.connector.connect', return_value=['a', 'nice', 'fancy', 'list']) as mock_connect:
        assert get_snowflake_connection(sfUser='user', sfPswd='password', sfURL='url', sfDatabase='database', sfSchema='schema', sfTable='table', sfRole='role') == ['a', 'nice', 'fancy', 'list']

        mock_connect.assert_called_with(user='user', password='password', account='url', database='database', schema='schema', role='role')


def test_get_pandas_dataframe():
    """Unit testing for get_pandas_dataframe"""

    mock_get_pandas_dataframe = create_autospec(get_pandas_dataframe, return_value='some pd_df')
    assert mock_get_pandas_dataframe(con='connector', sfDatabase='database', sfSchema='schema', sfTable='table', sfWarehouse='warehouse') == 'some pd_df'
    mock_get_pandas_dataframe.assert_called_with(con='connector', sfDatabase='database', sfSchema='schema', sfTable='table', sfWarehouse='warehouse')

    mock_get_pandas_dataframe = create_autospec(get_pandas_dataframe, return_value=['a', 'list'])
    assert mock_get_pandas_dataframe(con='connector', sfDatabase='database', sfSchema='schema', sfTable='table', sfWarehouse=None) == ['a', 'list']
    mock_get_pandas_dataframe.assert_called_with(con='connector', sfDatabase='database', sfSchema='schema', sfTable='table', sfWarehouse=None)

    with pytest.raises(ValueError):
        get_pandas_dataframe(con='connector', sfDatabase='database', sfSchema='schema', sfTable=None, sfWarehouse='warehouse')

    with pytest.raises(ValueError):
        get_pandas_dataframe(con='', sfDatabase='database', sfSchema='schema', sfTable='table', sfWarehouse='warehouse')


def test_get_snowflake_account_name():
    """Unit testing for get_snowflake_account_name"""

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


def test_get_profile_results():
    """Unit testing for get_profile_results"""

    mock_get_profile_results = create_autospec(get_profile_results, return_value='some profile')
    assert mock_get_profile_results('some pd_df') == 'some profile'
    mock_get_profile_results.assert_called_with('some pd_df')

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

















