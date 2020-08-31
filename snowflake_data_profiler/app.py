from flask import Flask
from snowflake_data_profiler.config import Config
from snowflake_data_profiler.routes.default import bp as default_blueprint
from flask_cors import CORS
#===========================================
# Create app and wire up routes 
#===========================================
# create and configure app
app = Flask(__name__, static_url_path='/', static_folder='static')
app.config.from_object(Config)
CORS(app)
# wire up routes with blueprints 
app.register_blueprint(default_blueprint, url_prefix='/report') # default route
#===========================================


# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=5000, debug=True)