from flask import Blueprint, request, url_for, current_app

from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.authors import Author, AuthorSchema
from api.utils.database import db
from flask_jwt_extended import jwt_required
import os
from werkzeug.utils import secure_filename

author_routes = Blueprint("author_routes", __name__)

allowed_extensions = ['gif', 'png', 'jpeg']


# def allowed_file(filename):
#     return filetype in allowed_extensions

basedir = os.path.abspath(os.path.dirname(__file__))

@author_routes.route('/avatar/<int:author_id>', methods=['POST'])
@jwt_required()
def upsert_author_avatar(author_id):
    try:
        file = request.files['avatar']
        filename = secure_filename(file.filename)
        file_ext = filename.split(".")[1]
        if file_ext not in allowed_extensions:
            return response_with(resp.INVALID_INPUT_423)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir, current_app.config['UPLOAD_FOLDER'], filename))
            # file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        get_author = Author.query.get_or_404(author_id)
        get_author.avatar = url_for('uploaded_file', filename=filename, _external=True)
        db.session.add(get_author)
        db.session.commit()
        author_schema = AuthorSchema()
        author = author_schema.dump(get_author)
        return response_with(resp.SUCCESS_200, value={"author": author})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_FIELD_NAME_SENT_422)

@author_routes.route('/', methods=['POST'])
@jwt_required()
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_423)


@author_routes.route('/', methods=['GET'])
def get_authors():
    try:
        authors_list = Author.query.all()
        author_schema = AuthorSchema(
            many=True, only=["id", "first_name", "last_name"])
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
        return response_with(resp.SUCCESS_200, value={"author": author})
    except Exception as e:
        print(e)
        return response_with(resp.BAD_REQUEST_400)


@author_routes.route('/<int:author_id>', methods=['PUT'])
@jwt_required()
def update_author_detail(author_id):
    data = request.get_json()
    get_author = Author.query.get_or_404(author_id)
    get_author.first_name = data['first_name']
    get_author.last_name = data['last_name']
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    result = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_201, value={"author": result})


@author_routes.route('/<int:author_id>', methods=['PATCH'])
@jwt_required()
def modify_author_detail(author_id):
    data = request.get_json()
    get_author = Author.query.get_or_404(author_id)
    if data.get('first_name'):
        get_author.first_name = data['first_name']
    if data.get('last_name'):
        get_author.last_name = data['last_name']
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    result = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_201, value={"author": result})


@author_routes.route('/<int:author_id>', methods=['DELETE'])
@jwt_required()
def delete_author(author_id):
    get_author = Author.query.get_or_404(author_id)
    db.session.delete(get_author)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
