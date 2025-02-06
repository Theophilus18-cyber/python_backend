from flask import Flask
from routes.user_routes import user_bp
from config import Config, db
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Load configuration from the Config class
app.config.from_object(Config)
# migrate 

migrate = Migrate(app,db)


# Initialize SQLAlchemy
db.init_app(app)

# Initialize CORS
CORS(app)

# Register the user routes blueprint
app.register_blueprint(user_bp)

# Swagger UI configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'User API'})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Import models after db is initialized
with app.app_context():
    from models.model import Model
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)