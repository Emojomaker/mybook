import requests
import json
import codecs
import collections
from flask import Flask, render_template, request, Response, make_response

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/auth', methods=['POST'])
def setcookies():
    if request.method == 'POST':
        user = request.form['login']
        password = request.form['password']
        auth_page = 'https://mybook.ru/api/auth/'
        auth_data = ({"email": user, "password": password})
        post = requests.post(auth_page, json=auth_data)
    return str(post.cookies)


def get_list_books():
    with open('data.txt') as f:
        json_data = json.load(f)
        keys_for_view = ['name', 'default_cover', 'authors_names']
        index = 0
        books = []
        while index >= 0:
            try:
                book = []
                for key in keys_for_view:
                    if key != 'authors_names':
                        book.append(json_data['objects'][index]['book'][key])
                    else:
                        book.append(json_data['objects'][index]['book'][key])
                books.append(book)
                index += 1
            except IndexError:
                index = -1
    return books


def iter_books(info=None):
    books = get_list_books()
    Book = collections.namedtuple('Book', 'name_book cover authors')
    book_for_user_list = []
    for elem in books:
        book = Book(name_book=elem[0],cover=elem[1],authors=elem[2])
        info = (f'Название книги: {book.name_book}, обложка: {book.cover}, авторы: {book.authors}')
        book_for_user_list.append(info)
    return render_template('mybooks.html', info=book_for_user_list)

if __name__ == '__main__':
     app.run(debug=True)
