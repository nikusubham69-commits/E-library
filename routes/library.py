from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import os

library_bp = Blueprint('library', __name__)
def init_library(book_model):
    @library_bp.route('/')
    def index():
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        books = book_model.get_all_books()
        return render_template('index.html', books=books, title="All Publications")

    # ADD THIS ROUTE HERE
    @library_bp.route('/my-wishlist')
    def my_wishlist():
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        
        # We call the model to get the data
        wishlisted_books = book_model.get_wishlist_for_user(session['user'])
        return render_template('index.html', books=wishlisted_books, title="My Read Later")
    
    # ... keep your other routes (add, wishlist/add, etc.)
    return library_bp