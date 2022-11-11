from flask import Blueprint

bookmarks = Blueprint('bookmarks', __name__, url_prefix='/api/v1/bookmarks')


@bookmarks.post('/')  # POST /api/v1/bookmarks
def get_all():
    return {"bookmarks": []}
