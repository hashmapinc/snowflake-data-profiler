from flask import Flask
from snowflake_data_profiler.config import Config
from snowflake_data_profiler.routes.default import bp as default_blueprint

#===========================================
# Create app and wire up routes 
#===========================================
# create and configure app
app = Flask(__name__)
app.config.from_object(Config)

# wire up routes with blueprints 
app.register_blueprint(default_blueprint) # default route
#===========================================


# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=5000, debug=True)