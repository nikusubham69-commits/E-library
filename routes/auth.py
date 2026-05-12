from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

def init_auth(user_model):
    @auth_bp.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = user_model.find_by_username(username)
            
            if user and check_password_hash(user['password'], password):
                session['user'] = user['username']
                session['role'] = user['role']
                return redirect(url_for('library.index'))
            flash("Invalid credentials", "danger")
        return render_template('login.html')

    @auth_bp.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if user_model.find_by_username(username):
                flash("User already exists", "danger")
            else:
                user_model.create_user(username, password)
                return redirect(url_for('auth.login'))
        return render_template('signup.html')

    @auth_bp.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('auth.login'))
    
    return auth_bp