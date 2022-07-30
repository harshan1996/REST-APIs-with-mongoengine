from flask import Response, request
from database.models import Books
from flask_restful import Resource

class BooksApi(Resource):
    def get(self):
        books = Books.objects().to_json()
        return Response(books, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        if Books.objects(book_id=body["book_id"]):
            return {"message": "book id {} already exists.Please enter a different book_id".format(body["book_id"])}
        else:
            book =  Books(**body).save()
            return {'message': 'successfully created book_id:{}'.format(book.book_id)}, 201
        
class BookApi(Resource):
    def put(self, book_id):
        body = request.get_json()
        Books.objects.get(book_id=book_id).update(**body)
        return {'message':'successfully updated book_id:{}'.format(book_id)}, 200
    
    def delete(self, book_id):
        book = Books.objects.get(book_id=book_id).delete()
        return {"message":"successfully deleted book_id:{}".format(book_id)}, 200

    def get(self, book_id):
        book = Books.objects.get(book_id=book_id).to_json()
        return Response(book,mimetype="application/json",status=200)