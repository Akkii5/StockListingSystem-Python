from flask import Blueprint, request, jsonify
from models.models import db, Stock
from flask_cors import CORS

stock_bp = Blueprint("stock", __name__, url_prefix="/api")  # Added url_prefix
CORS(stock_bp)

# ✅ Route to list stock types
@stock_bp.route("/stocks/types", methods=["GET"])  # Changed from "/api/stocks" to "/api/stocks/types"
def list_stock_types():
    return jsonify({"stock_types": ["NSE", "BSE", "Global"]})

# ✅ Route to add a new stock
@stock_bp.route("/stocks", methods=["POST"])
def add_stock():
    data = request.json
    required_fields = ["stock_type", "stock_id", "price_to_book_ratio", "price", "dividend_yield",
                       "company_name", "highest_price", "lowest_price", "price_margin"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    new_stock = Stock(**data)
    db.session.add(new_stock)
    db.session.commit()

    return jsonify({"message": "Stock added successfully", "stock_id": new_stock.stock_id}), 201

# ✅ Route to fetch stock by stock ID
@stock_bp.route("/stocks/id/<string:stock_id>", methods=["GET"])  # Changed endpoint to avoid conflict
def get_stock(stock_id):
    stock = Stock.query.filter_by(stock_id=stock_id).first()
    if not stock:
        return jsonify({"error": "Stock not found"}), 404
    return jsonify(stock.to_dict())

# ✅ Route to fetch stocks by stock type
@stock_bp.route("/stocks/type/<string:stock_type>", methods=["GET"])
def get_stocks_by_type(stock_type):
    stock_type = stock_type.upper()  # ✅ Convert input to uppercase
    stocks = Stock.query.filter_by(stock_type=stock_type).all()

    if not stocks:
        return jsonify({"error": f"No stocks found for {stock_type}"}), 404

    return jsonify([stock.to_dict() for stock in stocks])

