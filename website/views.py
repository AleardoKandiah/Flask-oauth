from flask import Blueprint

# def file blueprint
views = Blueprint('views', __name__)

# decorator and route
@views.route('/')
def home():
    return"<h1>Test</h1"