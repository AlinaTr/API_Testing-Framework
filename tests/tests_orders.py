from requests_folder.orders import submit_orders,get_all_orders, get_an_order, update_an_order, delete_an_order

class TestSubmitOrder:

    token = "c222e0152efecdb053b82b02ff61bffacdcc6ed4f97d7b7bf6ff6a1c148cad72"
# acest test pica
    def test_when_all_data_is_valid(self):
        response = submit_orders(5, 'AlinaTrandafir500',self.token)
        assert response.status_code == 201
        assert len(response.json())


    def test_when_token_is_associated_with_a_different_customer_name(self):
        response = submit_orders(6, "AlinaTranda", self.token)
        assert response.status_code == 201
        assert response.json()

    def test_when_book_is_not_in_stock(self):
        pass

class TestGetAllOrders:

    token = 'c222e0152efecdb053b82b02ff61bffacdcc6ed4f97d7b7bf6ff6a1c148cad72'
#pica
    def test_when_all_data_is_valid(self):
        response = get_all_orders(self.token)
        assert response.status_code == 200
        assert len(response.json())

class TestGetAnOrder:
# pica
    def test_when_all_data_is_valid(self):
       response= get_an_order("7wVJu5YKPZIkxAke1ZAla","c222e0152efecdb053b82b02ff61bffacdcc6ed4f97d7b7bf6ff6a1c148cad72")
       assert response.status_code == 200
       assert response.json()


class TestUpdateAnOrder:
    pass
# pica si in Postman

class TestDeleteAnOrder:
    pass