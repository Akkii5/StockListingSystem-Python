from flask import Flask
from flask_cors import CORS  # Import CORS
from models import db
from config import DATABASE_URI
from controllers.stock_controller import stock_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db.init_app(app)

# Enable CORS for all routes
CORS(app)

# Register Blueprints
app.register_blueprint(stock_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
