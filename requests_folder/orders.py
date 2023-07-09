import json

import requests

def submit_orders(book_id, customer_name, token):
    json_data = {

            "bookId": book_id,
            "customerName": customer_name
        }
    headers_data = {
        'Authorization': f'{token}'
    }
    response = requests.post(
        url='https://simple-books-api.glitch.me/orders',
        json=json_data,
        headers=headers_data,

    )
    return response

def get_all_orders(customer_name, customer_email, token):

    json_data = {

        "customerName": customer_name,
        "customerEmail": customer_email

    }
    headers_data = {
        'Authorization': f'{token}'
    }
    response = requests.get(
        url='https://simple-books-api.glitch.me/orders',
        json=json_data,
        headers=headers_data,

    )
    return response

def get_an_order(order_id, customer_name, customer_email, token):
    json_data = {

        "customerName": customer_name,
        "customerEmail": customer_email

    }
    headers_data = {
        'Authorization': f'{token}'
    }
    response = requests.get(
        url=f'https://simple-books-api.glitch.me/orders/{order_id}',
        json=json_data,
        headers=headers_data,

    )
    return response


def update_an_order(order_id, customer_name, token):
    json_data = {
        "customerName": customer_name
    }
    headers_data = {
        'Authorization': f'{token}'
    }
    response = requests.patch(
        url=f'https://simple-books-api.glitch.me/orders/{order_id}',
        json=json_data,
        headers=headers_data
    )

    return response


def delete_an_order(order_id, token):
    headers_data = {
        'Authorization': f'{token}'
    }

    response = requests.delete(
        url = f'https://simple-books-api.glitch.me/orders/{order_id}',
        headers = headers_data
    )

    return response


