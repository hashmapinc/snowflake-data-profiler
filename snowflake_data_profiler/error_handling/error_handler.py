def input_error(error):
    error = str(error)
    print(error)
    if '002003' in error and 'Database' in error:
        return 'Snowflake database is not authorized or does not exist'
    elif 'list index out of range' in error:
        return 'Please enter a value for Snowflake URL'
    elif '002003' in error and 'Schema' in error:
        return 'Snowflake schema is not authorized or does not exist'
    elif '002003' in error and 'Object' in error:
        return 'Snowflake table is not authorized or does not exist'
    elif '250001' in error:
        return 'Invalid Snowflake username, password, account, or role'
    elif '251006' in error:
        return 'Please enter a value for Snowflake password'
    elif '251005' in error:
        return 'Please enter a value for Snowflake username'
    elif '001003' in error and 'position 14' in error:
        return 'Please enter a value for Snowflake database'
    elif '002003' in error and 'PUBLIC' in error:
        return 'Please enter a value for Snowflake schema'
    elif '001003' in error and 'position 51' in error:
        return 'Please enter a value for Snowflake table'
    elif '251001' in error:
        return 'Please enter a value for Snowflake account'
    elif '002043' in error:
        return 'Snowflake warehouse is not authorized or does not exist'
    else:
        return 'Unknown Error'
