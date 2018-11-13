from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import json

from settings import *

app = Flask(__name__)
books = [
    {
        "name": "A",
        "price": 7.99,
        "isbn": 1
    },
    {
        "name": "B",
        "price": 17.99,
        "isbn": 2
    },
    {
        "name": "C",
        "price": 27.99,
        "isbn": 3
    },
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

@app.route("/books/<int:isbn>", methods=["DELETE"])
def delete_book(isbn):
    i = 0
    for book in books:
        if book["isbn"] == isbn:
            books.pop(i)
            response = Response("", status=204)
            return response
            # return jsonify(book)
        i += 1
    invalidBookObjectErrorMsg = {
        "error": "Book with the ISBN number was not found.",
        "helpString": "Data passed in similar to this {'name': 'bookname', 'price':7.33, 'isbn': 123}"
    }
    response = Response(json.dumps(invalidBookObjectErrorMsg), status=404, mimetype="application/json")
    return response


# PATCH
@app.route("/books/<int:isbn>", methods=["PATCH"])
def update_book(isbn):
    """
    PATCH - UPDATING
    Aktualizuje buď jméno nebo cenu nebo oboje.
    :param isbn:
    :return:
    """
    request_data = request.get_json()
    updated_book = {}
    if ("name" in request_data):
        updated_book["name"] = request_data["name"]
    if ("price" in request_data):
        updated_book["price"] = request_data["price"]
    for book in books:
        if book["isbn"] == isbn:
            book.update(updated_book)
    response = Response("", status=204)
    response.headers["Location"] = "/books/" + str(isbn)
    return response

# PUT
@app.route("/books/<int:isbn>", methods=["PUT"])
def replace_book(isbn):
    """
    PUT - REPLACING
    Změní/nahradí jméno a cenu pro celou knihu podle isbn.
    :param isbn:
    :return:
    """
    # return jsonify(request.get_json())
    request_data = request.get_json()
    if (not valid_put_request_data(request_data)):
        invalidBookObjectMsg = {
            "error": "Valid book object must be passed in the request",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price':7.33, 'isbn': 123}"
        }
    new_book = {
        "name": request_data["name"],
        "price": request_data["price"],
        "isbn": isbn
    }
    i = 0
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return response


def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

# POST /bookss
@app.route("/books", methods=["POST"])
def add_book():
    # return jsonify(request.get_json())
    request_data = request.get_json()
    if (validBookObject(request_data)):
        new_book = {
            "name": request_data["name"],
            "price": request_data["price"],
            "isbn": request_data["isbn"]
        }
        books.insert(0, new_book)
        response = Response("", 201, mimetype="application/json")
        response.headers["Location"] = "/books/" + str(new_book["isbn"])
        return response
        #return "True"
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object passed in request.",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price':7.33, 'isbn': 123}"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype="application/json")
        return response
        #return "False"

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