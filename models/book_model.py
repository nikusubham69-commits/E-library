from bson.objectid import ObjectId
from datetime import datetime

class BookModel:
    def __init__(self, db):
        self.collection = db['books']
        self.wishlist = db['wishlists']
        self.reviews = db['reviews']

    def get_all_books(self):
        return list(self.collection.find().sort("added_at", -1))

    def add_book(self, data):
        data['added_at'] = datetime.now()
        return self.collection.insert_one(data)

    def delete_book(self, book_id):
        return self.collection.delete_one({"_id": ObjectId(book_id)})

    def add_to_wishlist(self, username, book_id):
        return self.wishlist.update_one(
            {"user": username, "book_id": ObjectId(book_id)},
            {"$set": {"added_at": datetime.now()}},
            upsert=True
        )

    def add_review(self, book_id, username, rating, comment):
        return self.reviews.insert_one({
            "book_id": ObjectId(book_id),
            "user": username,
            "rating": int(rating),
            "comment": comment,
            "timestamp": datetime.now()
        })
    def get_wishlist_for_user(self, username):
        # 1. Find all wishlist entries for this user
        wish_items = list(self.wishlist.find({"user": username}))
        # 2. Extract the book IDs
        book_ids = [item['book_id'] for item in wish_items]
        # 3. Fetch the full book details from the main collection
        return list(self.collection.find({"_id": {"$in": book_ids}}))