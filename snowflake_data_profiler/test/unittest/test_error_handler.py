from snowflake_data_profiler.error_handling.error_handler import input_error

# python testing for error_handler.py
def test_input_error():

    result = input_error("002003 (02000): SQL compilation error: Database 'RQOJOQ' does not exist or not authorized.")
    assert result == 'Snowflake database is not authorized or does not exist'

    result = input_error("002003 (02000): SQL compilation error: Schema 'FIVETRAN_DB.VADA' does not exist or not authorized.")
    assert result == 'Snowflake schema is not authorized or does not exist'

    result = input_error("002003 (42S02): SQL compilation error: Object 'FIVETRAN_DB.RANDY_SYNAPSE_COMPARISON.DIM_CUSTOMERS' does not exist or not authorized.")
    assert result == 'Snowflake table is not authorized or does not exist'

    result = input_error('250001 (08001): Failed to connect to DB: hashmap.snowflakecomputing.com:443. Incorrect username or password was specified.')
    assert result == 'Invalid Snowflake username, password, account, or role'

    result = input_error("002043 (02000): SQL compilation error: Object does not exist, or operation cannot be performed.")
    assert result == 'Snowflake warehouse is not authorized or does not exist'

    result = input_error('shape mismatch: its a square not a circle')
    assert result == f'Congratulations, you found a bug! This bug is our top priority right now and has to do with how your table data is being read by our Python backend. We have had luck rerunning the profile request, so please give it another try. Otherwise, you can leave feedback above and we will reach out when we figure out how to fix this.\n\nError: shape mismatch: its a square not a circle'

    result = input_error('something random: random error randomly generated')
    assert result == "Lucky you! There's been an unknown error: something random: random error randomly generated\n\nReach out to randy.pitcher@hashmapinc.com if you'd like to chat about this error or maybe you could try again (our profiling library is still maturing). Thanks!"

    result = input_error('')
    assert result == "Lucky you! There's been an unknown error: \n\nReach out to randy.pitcher@hashmapinc.com if you'd like to chat about this error or maybe you could try again (our profiling library is still maturing). Thanks!"
