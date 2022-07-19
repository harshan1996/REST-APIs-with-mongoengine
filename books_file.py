from mongoengine import IntField, StringField, Document


class books(Document):
    book_id = IntField()
    book_name = StringField(max_length=50)
    author = StringField(max_length=30)
    number_of_pages = IntField(max_value=2000)

    def to_json(self):
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "author": self.author,
            "number_of_pages": self.number_of_pages
        }
