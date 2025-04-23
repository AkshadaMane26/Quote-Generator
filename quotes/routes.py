from flask import Blueprint, request, jsonify, render_template
from .service import get_random_quote, get_quote_by_author, get_authors, add_quote

bp = Blueprint("quotes", __name__)

@bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@bp.route("/quote", methods=["GET"])
def get_quote():
    author = request.args.get("author")
    if author:
        quotes = get_quote_by_author(author)
        if quotes:
            return jsonify(quotes), 200
        return jsonify({"error": "No quotes found for this author"}), 404
    return jsonify(get_random_quote()), 200

@bp.route("/quote", methods=["POST"])
def post_quote():
    data = request.get_json()
    if not data or "quote" not in data or "author" not in data:
        return jsonify({"error": "Both 'quote' and 'author' are required"}), 400
    return jsonify({
        "message": "Quote added successfully",
        "quote": add_quote(data)
    }), 201

@bp.route("/authors", methods=["GET"])
def get_authors_route():
    authors = get_authors()
    return jsonify(authors), 200


    

