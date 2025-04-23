from flask import Flask
from models.models import db
from config import DATABASE_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db.init_app(app)

with app.app_context():
    db.create_all()