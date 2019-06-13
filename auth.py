import requests
import requests_cache
import re
import json
import codecs
import unicodedata
import collections

user = request.form['login']
password = request.form['password']
auth_page = 'https://mybook.ru/api/auth/'
auth_data = ({"email": user, "password": password})
post = requests.post(auth_page, json=auth_data)

def getinfo():
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

def iter():
    books = getinfo()
    Book = collections.namedtuple('Book', 'name_book cover authors')
    for elem in books:
        book = Book(name_book=elem[0],cover=elem[1],authors=elem[2])
        info = (f'Название книги: {book.name_book}, обложка: {book.cover}, авторы: {book.authors}')
        yield info

for elem in iter():
    print(elem)


