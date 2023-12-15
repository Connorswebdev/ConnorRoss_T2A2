
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from models.user import User
from init import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    return render_template('login.html', user=current_user)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        if password != password_confirmation:
            flash('Passwords do not match', category='error')
        elif password is None or len(password) < 7:
            flash('Password must be longer than 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account successfully created', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)