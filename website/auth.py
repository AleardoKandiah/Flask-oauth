from flask import Blueprint

# def file blueprint
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login</p>"


@auth.route('/logout')
def login():
    return "<p>logout</p>"

@auth.route('/Sign-up')
def login():
    return "<p>Sign Up/p>"

