from crypt import methods
from mongoengine import connect
from books_file import books
from flask import Flask, jsonify, request

application = Flask(__name__)

connect(db="firstAtlasDB", host="mongodb+srv://Harshan:Password@firstcluster.zxdpy3p.mongodb.net/?retryWrites=true&w=majority", alias="default")


@application.route("/books/createBook", methods=['GET', 'POST'])
def create_books():
    request_data = request.get_json()
    output_data = {
        "book_id": request_data["book_id"],
        "book_name": request_data["book_name"],
        "author": request_data["author"],
        "number_of_pages": request_data["number_of_pages"]
    }
    if books.objects(book_id=request_data["book_id"]):
        return jsonify({"message": "book id {} already exists.Please enter a different book_id".format(request_data["book_id"])})
    else:
        current_book = books(book_id=output_data["book_id"], book_name=output_data["book_name"],author=output_data["author"], number_of_pages=output_data["number_of_pages"])
        current_book.save()
        return jsonify(output_data,{"message": "successfully saved.book id {}".format(request_data["book_id"])})

@application.route("/books", methods=['GET'])
def get_all_books():
    all_books = books.objects
    return jsonify(all_books.to_json(), {"message":"Total number of books {}".format(books.objects.count())})


@application.route("/books/<int:book_id>", methods=['GET', 'POST'])
def get_a_book(book_id):
    if request.method == 'GET':
        single_book = books.objects(book_id=book_id).first()
        if single_book:
            return jsonify(single_book.to_json())


@application.route("/books/<int:book_id>", methods=['PUT'])
def update_book(book_id):
    if request.method == 'PUT':
        fetch_the_data = request.get_json()  # works with .json too
        update_book = books.objects(book_id=book_id).first()
        update_book.update(
            book_name=fetch_the_data['book_name'], author=fetch_the_data['author'], number_of_pages=fetch_the_data['number_of_pages'])
        return jsonify({"message": "successfully updated.book id {}".format(book_id)})


@application.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    if request.method == 'DELETE':
        delete_book = books.objects(book_id=book_id).first()
        delete_book.delete()
        return jsonify({"message": "successfully deleted.book id {}".format(book_id)})


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000, debug=True)
