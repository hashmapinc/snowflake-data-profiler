def input_error(error):
    error = str(error)
    print(error)
    if '002003' and 'Database' in error:
        return 'Snowflake database is not authorized or does not exist'
    elif '002003' and 'Schema' in error:
        return 'Snowflake schema is not authorized or does not exist'
    elif '002003' and 'Object' in error:
        return 'Snowflake table is not authorized or does not exist'
    elif '250001' in error:
        return 'Incorrect Snowflake username, password, or account'
    elif '251006' in error:
        return 'Please enter a value for Snowflake password'
    elif '251005' in error:
        return 'Please enter a value for Snowflake username'
    elif '001003' and 'position 14' in error:
        return 'Please enter a value for Snowflake database'
    elif '002003' and 'PUBLIC' in error:
        return 'Please enter a value for Snowflake schema'
    elif '001003' and 'position 51' in error:
        return 'Please enter a value for Snowflake table'
    elif '251001' in error:
        return 'Please enter a value for Snowflake account'
    else:
        return
