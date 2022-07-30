from .books import BooksApi, BookApi

def initialize_routes(api):
    api.add_resource(BooksApi, '/api/books')
    api.add_resource(BookApi, '/api/books/<int:book_id>')