from flask import Blueprint, request

from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.authors import Author, AuthorSchema
from api.utils.database import db

author_routes = Blueprint("author_routes", __name__)

@author_routes.route('/', methods=['POST'])
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        print(e) 
        return response_with(resp.INVALID_INPUT_422)
    

@author_routes.route('/', methods=['GET'])    
def get_authors():
    try:
        authors_list = Author.query.all()
        author_schema = AuthorSchema(many=True, only=["id", "first_name", "last_name"])
        authors = author_schema.dump(authors_list)
        return response_with(resp.SUCCESS_200, value={"authors": authors})
    except print(0):
        print(e)
        return response_with(resp.BAD_REQUEST_400)
    
@author_routes.route('/<int:author_id>', methods=['GET'])
def get_author(author_id):
    try:
        fetched = Author.query.get_or_404(author_id)
        author_schema = AuthorSchema()
        author = author_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, {"author": author})
    except Exception as e:
        print(e)
        return response_with(resp.BAD_REQUEST_400)
    
@author_routes.route('/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    data = request.get_json()
    get_author = Author.query.get_or_404(author_id)
    
