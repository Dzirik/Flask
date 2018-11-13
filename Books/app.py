from flask import Flask
from flask import jsonify

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

# GET /books
@app.route("/books")
def get_books():
    return jsonify({"books": books})

@app.route("/")
def hello_world():
    return "Hello world"

app.run(port=5000)