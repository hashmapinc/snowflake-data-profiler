import pandas as pd
from datetime import datetime
from pandas_profiling import ProfileReport
from snowflake import connector


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


def connect_to_snowflake(sfUser, sfPswd, sfAccount, sfWarehouse, sfDatabase, sfSchema, sfTable):

    con = connector.connect(
        user=sfUser,
        password=sfPswd,
        account=sfAccount,
        warehouse=sfWarehouse,
        database=sfDatabase,
        schema=sfSchema,
    )

    cur = con.cursor()

    cur.execute(f'select * from {sfDatabase}.{sfSchema}.{sfTable};')

    df = cur.fetch_pandas_all()

    return df


def get_profile_results(data):
    profile = ProfileReport(data, title='Pandas Profile Report')

    now = datetime.now()

    profile.to_file(output_file=f"my_data/pandas_profiling_{now}.html")

    return f"http://localhost:63342/snowflake-data-profiler/my_data/pandas_profiling_{now}.html"


def main():
    pd_df = connect_to_snowflake()

    return get_profile_results(pd_df)


if __name__ == "__main__":
    main()

