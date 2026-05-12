from flask import Flask
from pymongo import MongoClient
from models.user_model import UserModel
from models.book_model import BookModel
from routes.auth import auth_bp, init_auth
from routes.library import library_bp, init_library
import os

app = Flask(__name__)

# SECURITY: Use an environment variable for the secret key on Render
app.secret_key = os.getenv("SECRET_KEY", "nexus_secret_default_change_me")

# DB Connection Logic
# We pull the URL from environment variables for Render, or use local/hardcoded as fallback
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://nikusubham69_db_user:Subham2002@cluster0.csltnyd.mongodb.net/")

# Connect to the client
client = MongoClient(MONGO_URL)

# Define the 'db' variable specifically
# Replace 'elibrary_db' with whatever name you want your database to have in Atlas
db = client['elibrary_db']

# Init Models - Now 'db' is correctly defined above
user_m = UserModel(db)
book_m = BookModel(db)

# Register Blueprints
# We pass the initialized models into the blueprints
app.register_blueprint(init_auth(user_m))
app.register_blueprint(init_library(book_m))

# Root route redirect (Optional: ensures '/' always works)
@app.route('/health')
def health():
    return {"status": "online"}, 200

if __name__ == '__main__':
    # For local testing
    app.run(debug=True, use_reloader=False)