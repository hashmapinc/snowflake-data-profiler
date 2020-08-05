def input_error(err):
    error = str(err)
    if '002003' in error and 'Database' in error:
        return 'Snowflake database is not authorized or does not exist'
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
    elif error.startswith('shape mismatch:'):
        return f'Congratulations, you found a bug! This bug is our top priority right now and has to do with how your table data is being read by our Python backend. We have had luck rerunning the profile request, so please give it another try. Otherwise, you can leave feedback above and we will reach out when we figure out how to fix this.\n\nError: {error}'
    else:
        return f"Lucky you! There's been an unknown error: {error}\n\nReach out to randy.pitcher@hashmapinc.com if you'd like to chat about this error or maybe you could try again (our profiling library is still maturing). Thanks!"
