from flask import render_template, request, Response, Blueprint, url_for, jsonify
from snowflake_data_profiler.profiling.profiler import get_profile
from snowflake_data_profiler.error_handling.error_handler import input_error


#==============================================================================
# default API 
#==============================================================================
# define namespace
bp = Blueprint('default', __name__)


@bp.route('/', methods=['POST'])
def post_data():
    """default post handler"""
    resp = {}
    try:
        req       = request.form
        username  = req.get('username')
        password  = req.get('password')
        url       = req.get('url')
        role      = req.get('role')
        warehouse = req.get('warehouse')
        database  = req.get('database')
        schema    = req.get('schema')
        table     = req.get('table')
        profile_page = get_profile(username, password, url, database, schema, table, role, warehouse)

    except Exception as e:
        print(e)
        resp['status'] = 'error'
        resp['error'] = input_error(e)
        return jsonify(resp)

    resp['status'] = 'ok'
    resp['profile_report'] = profile_page
    return jsonify(resp)
#==============================================================================






