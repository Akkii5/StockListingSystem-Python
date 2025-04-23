from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_type = db.Column(db.String(10), nullable=False)  # NSE, BSE, Global
    stock_id = db.Column(db.String(50), unique=True, nullable=False)
    price_to_book_ratio = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    dividend_yield = db.Column(db.Float, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    highest_price = db.Column(db.Float, nullable=False)
    lowest_price = db.Column(db.Float, nullable=False)
    price_margin = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
