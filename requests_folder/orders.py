import requests

def submit_orders(book_id, customer_name, token):

    json_data = {

            "bookId": book_id,
            "customerName": customer_name
        }

    headers_data = {
        'Authorization': f'Bearer: {token}'
    }

    response = requests.post(
        url='https://simple-books-api.glitch.me/orders',
        json=json_data,
        headers=headers_data
    )

    return response