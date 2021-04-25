from flask import Blueprint, request

from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.books import Book, BookSchema
from api.utils.database import db
from api.models.authors import AuthorSchema
from flask_jwt_extended import jwt_required

book_routes = Blueprint("book_routes", __name__)


@book_routes.route('/', methods=['POST'])
# @jwt_required
def new_book():
    try:
        data = request.get_json()
        book_schema = BookSchema()
        book = book_schema.load(data)
        result = book_schema.dump(book.create())
        return response_with(resp.SUCCESS_201, value={"book": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@book_routes.route('/', methods=['GET'])
def fetch_books():
    fetched = Book.query.all()
    book_schema = BookSchema(many=True, only=['author_id','title', 'year'])
    books = book_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"books": books})


@book_routes.route('/<int:id>', methods=['GET'])
def get_book_detail(id):
    get_book = Book.query.get_or_404(id)
    book_schema = BookSchema()
    result = book_schema.dump(get_book)
    return response_with(resp.SUCCESS_200, value={"book": result})


@book_routes.route('/<int:id>', methods=['PUT'])
# @jwt_required
def book_details_update(id):
    data = request.get_json()
    fetch_book = Book.query.get_or_404(id)
    fetch_book.title = data['title']
    fetch_book.year = data['year']
    db.session.add(fetch_book)
    db.session.commit()
    book_schema = BookSchema()
    result = book_schema.dump(fetch_book)
    return response_with(resp.SUCCESS_201, value={"book": result})


@book_routes.route('/<int:id>', methods=['PATCH'])
# @jwt_required
def book_details_modify(id):
    data = request.get_json()
    get_book = Book.query.get_or_404(id)
    if data.get('title'):
        get_book.title = data['title']
    if data.get('year'):
        get_book.year = data['year']
    db.session.add(get_book)
    db.session.commit()
    book_schema = BookSchema()
    book = book_schema.dump(get_book)
    return response_with(resp.SUCCESS_200, value={"book": book})


@book_routes.route('/<int:id>', methods=['DELETE'])
# @jwt_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
