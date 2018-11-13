from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
books = [
    {
        "name": "Green Eggs and Ham",
        "price": 7.99,
        "isbn": 123456
    },
    {
        "name": "The Cat in the Hat",
        "price": 6.99,
        "isbn": 234567
    }
]

# POST /books
@app.route("/books", methods=["POST"])
def add_book():
    return jsonify(request.get_json())

# GET /books/<isbn>
@app.route("/books/<int:isbn>")
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                "name": book["name"],
                "price": book["price"]
            }
    return jsonify(return_value)

# GET /books
@app.route("/books")
def get_books():
    return jsonify({"books": books})

@app.route("/")
def initial_page():
    return "<b><font size=\"+2\"> This is an intial page of Books Application </font></b>"

app.run(port=5000)