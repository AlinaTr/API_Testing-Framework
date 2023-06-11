from requests_folder.orders import submit_orders,get_all_orders, get_an_order, update_an_order, delete_an_order

class TestSubmitOrder:

    # token = '6770bcac03389e9765e52186da2a168dc19c7574a7ba436f7fb9b5d5f1ce11c9'
    #
    # def test_when_all_data_is_valid(self):
    #     response = submit_orders(1, 'AlinaTrandafir1111',self.token)

    def test_when_token_is_associated_with_a_different_customer_name(self):
        pass

class TestGetAllOrders:

    token = '208873f3fcc3963675d91e7f4de7d06502e9719ad9deee8ef7d6db3036ac6ba0'

    def test_when_all_data_is_valid(self):
        response = get_all_orders('AlinaTrandafir115', 'alina115@example.com', self.token)
        assert response.status_code == 200
        assert response.json()

class TestGetAnOrder:

    def test_when_all_data_is_valid(self):
       response= get_an_order("jH2GCbEPPflJ1H4k4KV_K", "AlinaTrandafir115", "alina115@example.com", "208873f3fcc3963675d91e7f4de7d06502e9719ad9deee8ef7d6db3036ac6ba0")
       assert response.status_code == 200
       assert response.json()


class TestUpdateAnOrder:
    pass

class TestDeleteAnOrder:
    pass