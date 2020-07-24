from flask import render_template, request, Response, Blueprint
from snowflake_data_profiler.profiling.profiler import connect_to_snowflake, get_profile_results
from snowflake_data_profiler.error_handling.error_handler import input_error

#==============================================================================
# default API 
#==============================================================================
# define namespace
bp = Blueprint('default', __name__)

# default get handler
@bp.route('/', methods=['GET'])
def get_profile():
    return render_template('profile.html', title='Profiler')

# default post handler
@bp.route('/', methods=['POST'])
def post_profile():

    try:
        req = request.form
        username = req.get('username')
        password = req.get('password')
        account = req.get('account')
        warehouse = req.get('warehouse')
        database = req.get('database')
        schema = req.get('schema')
        table = req.get('table')
        pd_df = connect_to_snowflake(username, password, account, warehouse, database, schema, table)
        profile_page = get_profile_results(pd_df)

    except Exception as e:
        error = input_error(e)
        return render_template('profile.html', title='Error Occurred', error=error)

    return Response(profile_page, mimetype='text/html')
#==============================================================================






