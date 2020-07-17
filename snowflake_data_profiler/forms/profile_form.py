from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class ProfileForm(FlaskForm):
    username  = StringField('Snowflake Username', validators=[DataRequired()])
    password  = PasswordField('Snowflake Password', validators=[DataRequired()])
    account   = StringField('Snowflake Account', validators=[DataRequired()])
    warehouse = StringField('Snowflake Warehouse', validators=[DataRequired()])
    database  = StringField('Snowflake Database', validators=[DataRequired()])
    schema    = StringField('Snowflake Schema', validators=[DataRequired()])
    table     = StringField('Snowflake Table', validators=[DataRequired()])
    submit    = SubmitField('Create Profile')