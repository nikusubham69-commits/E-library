from werkzeug.security import generate_password_hash

class UserModel:
    def __init__(self, db):
        self.collection = db['users']

    def find_by_username(self, username):
        return self.collection.find_one({"username": username})

    def create_user(self, username, password):
        role = "admin" if username.lower() == "admin" else "user"
        hashed_pw = generate_password_hash(password)
        return self.collection.insert_one({
            "username": username,
            "password": hashed_pw,
            "role": role
        })