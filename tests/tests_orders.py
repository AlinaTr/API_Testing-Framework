from requests_folder.orders import submit_orders

class TestSubmitOrder:

    token = '6770bcac03389e9765e52186da2a168dc19c7574a7ba436f7fb9b5d5f1ce11c9'

    def test_submit_order_when_all_data_is_valid(self):
        response = submit_orders(1, 'AlinaTrandafir1111',self.token)