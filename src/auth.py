from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth.post('/register')  # POST /api/v1/auth/register
def register():
    return "User created"


@auth.get('/me')  # GET /api/v1/auth/me
def me():
    return {"User": "me"}
