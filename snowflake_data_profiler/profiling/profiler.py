import pandas as pd
from pandas_profiling import ProfileReport
from snowflake import connector


def get_snowflake_account_name(sfURL):
    """parses snowflake url if given a url"""

    # check if this is a url or already is an account name
    if '.snowflakecomputing.com' not in sfURL:
        return sfURL # assume that without the domain, this is already an account name

    # extract the http(s):// if it exists
    stripped_url = sfURL.split('://')[1] if '://' in sfURL else sfURL

    # pull out the account name now that we have the stripped url
    account_name = stripped_url.split('.snowflakecomputing.com')[0]

    return account_name


def file_to_df(file_name):
    if file_name.endswith('.csv'):
        df = pd.read_csv(file_name)
    elif file_name.endswith('.xlsx'):
        df = pd.read_excel(file_name)
    elif file_name.endswith('.json'):
        df = pd.read_json(file_name)
    elif file_name.endswith('.sql'):
        df = pd.read_sql(file_name)
    elif file_name.endswith('.html'):
        df = pd.read_html(file_name)
    elif file_name.endswith('.sql'):
        df = pd.read_sql(file_name)
    return df


def get_snowflake_connection(sfUser, sfPswd, sfURL, sfDatabase, sfSchema, sfTable, sfRole=None):
    """establishes snowflake connection and returns connector object"""

    if not sfUser or not sfPswd or not sfURL or not sfDatabase or not sfSchema or not sfTable:
        raise ValueError('A required variable has not been added.')

    sfAccount = get_snowflake_account_name(sfURL)
    
    con = connector.connect(
        user=sfUser,
        password=sfPswd,
        account=sfAccount,
        database=sfDatabase,
        schema=sfSchema,
        role=sfRole,
    )
    return con


def get_pandas_dataframe(con, sfDatabase, sfSchema, sfTable, sfWarehouse=None):
    """creates cursor object and returns a pandas dataframe from the Snowflake table"""

    cur = con.cursor()
    if sfWarehouse:
        cur.execute(f'use warehouse {sfWarehouse};')

    cur.execute(f'select * from {sfDatabase}.{sfSchema}.{sfTable} limit 10000;')
    df = cur.fetch_pandas_all()

    return df


def get_profile_results(data):
    """profiles pandas dataframe"""

    if isinstance(data, pd.DataFrame):
        profile = ProfileReport(
          data,
          title='Snowflake Data Profiler from Hashmap',
          progress_bar=False,
          explorative=True,
          correlations={
             "pearson": {"calculate": True},
             "spearman": {"calculate": False},
             "kendall": {"calculate": False},
             "phi_k": {"calculate": False},
             "cramers": {"calculate": False},
         },
        )

        p = profile.to_html() # this step sometimes fails with matplotlib errors about threads. I've only fixed it by adjusting requirements.txt in the past. I've just specified the specific versions of libraries. Pyarrow seems to have an impact on this.
        return p

    else:
        raise TypeError('This is not a pandas dataframe.')


def get_profile(sfUser, sfPswd, sfURL, sfDatabase, sfSchema, sfTable, sfRole=None, sfWarehouse=None):
    """main function"""

    conn = get_snowflake_connection(sfUser, sfPswd, sfURL, sfDatabase, sfSchema, sfTable, sfRole)
    pd_df = get_pandas_dataframe(conn, sfDatabase, sfSchema, sfTable, sfWarehouse)
    return get_profile_results(pd_df)


