from flask import Blueprint, render_template, request, flash
from flask_login import current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    return render_template('login.html', user=current_user)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        if password != password_confirmation:
            flash('Passwords do not match', category='error')
        elif len(password) < 7:
            flash('Password must be longer than 7 characters', category='error')
        else:
            flash('Account successfully created', category='success')

    return render_template('sign_up.html', user=current_user)
