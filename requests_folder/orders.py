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
        headers=headers_data,

    )

    return response

def get_all_orders(client_name, client_email,token):

    json_data={
        "clientName": client_name,
        "clientEmail": client_email

    }

    headers_data={
        'Authorization':f'Bearer:{token}'
    }


    response = requests.get(
        url='https://simple-books-api.glitch.me/orders',
        json = json_data,
        headers=headers_data

    )
    return response

def get_an_order(order_id,client_name, client_email, token):

    json_data= {
   "clientName": client_name,
   "clientEmail": client_email
}

    headers_data= {
        'Authorization': f'Bearer: {token}'
    }

    url = f'https://simple-books-api.glitch.me/orders/{order_id}'

    response= requests.get(
        url=url,
        json_data=json_data,
        headers_data=headers_data

    )
    return response


def update_an_order(order_id, client_name, client_email, token):

    json_data={
  "customerName": client_name
    }

    headers_data={
        'Authorization':f'Bearer:{token}'
    }

    url= f'https://simple-books-api.glitch.me/orders/{order_id}'
    response= requests.patch(
        url=url,
        json_data=json_data,
        headers_data=headers_data
    )
    return response

def delete_an_order(order_id, token):
    pass


