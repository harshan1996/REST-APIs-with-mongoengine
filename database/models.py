from .db import db

class Books(db.Document):
    book_id = db.IntField()
    book_name = db.StringField(max_length=50)
    author = db.StringField(max_length=30)
    number_of_pages = db.IntField(max_value=2000)
        