from flask import render_template, redirect, request
from app import app
from app.forms import ProfileForm
from profiling import connect_to_snowflake, get_profile_results


@app.route('/', methods=['POST'])
def post_profile():

    form = ProfileForm()

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

    except Exception as error:
        print(error)
        return render_template('profile.html', title='Error Occurred', form=form, error=error)

    return redirect(profile_page)


@app.route('/', methods=['GET'])
def get_profile():

    form = ProfileForm()

    return render_template('profile.html', title='Profiler', form=form)






