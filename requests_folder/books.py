import requests

# GET request
# requests.get(...)

# POST
# requests.post(....)

def get_all_books(type = None, limit = None): # None=  optional parameters
    url = 'https://simple-books-api.glitch.me/books'
    if bool(type) and bool(limit):
        #https://simple-books-api.glitch.me/books?type=fiction&limit=0
        # modificam url de baza la care adaugam partea de mai sus|:
        # https://simple-books-api.glitch.me/books?type=fiction&limit=0 + ?type=fiction&limit=0
        url += f'?type={type}&limit={limit}'
    elif bool(type):
        url += f'?type={type}'
    elif bool(limit):
        url += f'?limit={limit}'
    response = requests.get(url= url)
    print(response.json())
    print(response.status_code)
    return response

# get_all_books('non-fiction')
# print('======================')
# get_all_books()
# print('======================')
# get_all_books('fiction', 1)
# print('======================')
# get_all_books(limit = 2)
# print('===============')

def get_book_by_id(book_id):
    url = f'https://simple-books-api.glitch.me/books/{book_id}'
    response = requests.get(url = url)
    return response
