from requests_folder.orders import submit_orders, get_all_orders, get_an_order, update_an_order, delete_an_order


class TestSubmitOrder:

    token = "da7ffdc096b4a5d28eca684a21fe9caf248c2722238393dfc7a16f7176a2b763"

    def test_when_all_data_is_valid(self):
        response = submit_orders(5, 'alinatr502',self.token)
        assert response.status_code == 201
        assert len(response.json())


    def test_when_token_is_associated_with_a_different_customer_name(self):
        response = submit_orders(6, "CristinaC", self.token)
        assert response.status_code == 201
        assert response.json()

        """ Tests bug reports:
            test_when_token_is_associated_with_a_different_customer_name nu functioneaza corespunzator cand ia ca 
            parametru un alt user, decat cel asociat cu token
            => se genereaza order, in loc sa primim eroare

            """

    def test_when_book_id_is_valid_and_book_does_not_exist_in_db(self):
        response = submit_orders(7, 'alinatr502', self.token)
        assert response.status_code == 400
        response_data = response.json()
        expected = "Invalid or missing bookId."
        actual = response_data.get('error')
        assert expected == actual

    def test_when_providing_incorrect_token(self):
        response = submit_orders(5, 'alinatr502', 'ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58')
        assert response.status_code == 401
        assert response.json()

class TestGetAllOrders:

    token = 'da7ffdc096b4a5d28eca684a21fe9caf248c2722238393dfc7a16f7176a2b763'

    def test_when_all_data_is_valid(self):
        response = get_all_orders('alinatr502', 'alina502@example.com' , self.token)
        assert response.status_code == 200
        assert len(response.json())

    def test_when_token_is_invalid(self):
        response = get_all_orders('alinatr502', 'alina502@example.com','ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58a')
        assert response.status_code == 401
        assert len(response.json())

    def test_when_providing_invalid_username_and_valid_email_and_valid_token(self):
        response =  get_all_orders('alinatr5555', 'alina502@example.com', self.token)
        assert response.status_code == 200
        assert len(response.json())
    """
        Test Bug report
        - when providing invalid username but valid email address and valid token, 
        - we still receive the list of orders
        => see test_when_providing_invalid_username_and_valid_email_and_valid_token
    """
    def test_when_providing_valid_username_and_invalid_email_and_valid_token(self):
        response = get_all_orders('alinatr502', 'al@example.com', self.token)
        assert response.status_code == 200
        assert len(response.json())

        """
                Test Bug report
                - when providing invalid email address but valid username address and valid token, 
                - we still receive the list of orders
                => see test_when_providing_valid_username_and_invalid_email_and_valid_token
            """

    def test_when_providing_invalid_username_and_invalid_password_and_invalid_token(self):
        response = get_all_orders('al2', 'al@example.com','ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58')
        assert response.status_code == 401
        assert response.json()

    def test_when_providing_invalid_username_and_invalid_password_and_valid_token(self):
        response = get_all_orders('al', 'al@example.com', self.token)
        assert response.status_code == 200
        assert len(response.json())

        """
         Test Bug report
            - when providing invalid email address and invalid username, but valid token, 
            - we still receive the list of orders
            => see test_when_providing_invalid_username_and_invalid_password_and_valid_token
                    """

class TestGetAnOrder:
    token = 'da7ffdc096b4a5d28eca684a21fe9caf248c2722238393dfc7a16f7176a2b763'


    def test_when_all_data_is_valid(self):
        response = get_an_order('HPAUjVC7ZopJzIJli0UKu','alinatr502', '"alinatr502@example.com',  self.token)
        assert response.status_code == 200
        assert response.json()


    def test_without_token(self):
        response = get_an_order('HPAUjVC7ZopJzIJli0UKu','alinatr502', 'alinatr502@example.com', '')
        assert response.status_code == 401
        assert response.json()

    def test_when_token_is_invalid(self):
        response = get_an_order('HPAUjVC7ZopJzIJli0UKu','alinatr502', 'alina502@example.com','ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58a')
        assert response.status_code == 401
        assert len(response.json())

    def test_when_providing_invalid_username_and_valid_order_id_valid_email_and_valid_token(self):
        response = get_an_order('HPAUjVC7ZopJzIJli0UKu','al', 'alina502@example.com', self.token)
        assert response.status_code == 200
        assert len(response.json())

    """
        Test Bug report
        - when providing invalid username but valid email address and valid token, 
        - we still get the order
        => see test_when_providing_invalid_username_and_valid_email_and_valid_token
    """

    def test_when_providing_invalid_order_id_and_valid_credentials_and_data(self):
        response = get_an_order('HPAUjVC7ZopJzIJli0UK', 'alinatr502', 'alina502@example.com', self.token)
        assert response.status_code == 404
        assert response.json()


class TestUpdateAnOrder:
    token = 'da7ffdc096b4a5d28eca684a21fe9caf248c2722238393dfc7a16f7176a2b763'

    def test_when_all_data_is_valid(self):
        response = update_an_order('kn9rCNtfEhFbCH7ysPCSL', 'alinatr502', self.token)
        assert response.status_code == 204
        assert response.text == ''

    def test_when_order_id_is_invalid(self):
        response = update_an_order('HPAUjVC7ZopJzIJli0UK', 'alinatr502', self.token)
        assert response.status_code == 404
        assert response.json()

    def test_when_order_id_and_token_are_invalid(self):
        response = update_an_order('SdA4xMm6ZOajfP0mTp', 'alinatr502', 'ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58a')
        assert response.status_code == 401
        response_data = response.json()
        expected = "Invalid bearer token."
        actual = response_data.get('error')
        assert expected == actual

    def test_when_token_is_invalid(self):
        response = update_an_order('8y_SdA4xMm6ZOajfP0mTp', 'alinatr502', 'ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58a')
        assert response.status_code == 401
        response_data = response.json()
        expected = "Invalid bearer token."
        actual = response_data.get('error')
        assert expected == actual

    def test_when_username_is_invalid(self):
        response = update_an_order('8LiQ7ffTHnbBJHAgycnVM', 'al', self.token)
        assert response.status_code == 204
        assert response.text == ''

class TestDeleteAnOrder:
    token = 'da7ffdc096b4a5d28eca684a21fe9caf248c2722238393dfc7a16f7176a2b763'

    def test_when_all_data_is_valid(self):
        response = delete_an_order('sMN_WCz6nTj51C3Zexu51', self.token)
        assert response.status_code == 404
        response_data = response.json()
        expected = None
        actual = response_data.get(None)
        assert expected == actual


    def test_when_order_has_already_been_deleted(self):
        response = delete_an_order('FYkZMM0d1kES5r5WZF0pm', self.token)
        assert response.status_code == 404
        response_data = response.json()
        expected = "No order with id FYkZMM0d1kES5r5WZF0pm."
        actual =  response_data.get('error')
        assert expected == actual

    def test_when_order_id_is_invalid(self):
        response = delete_an_order('FYkZMM0d1', self.token)
        assert response.status_code == 404
        response_data = response.json()
        expected = "No order with id FYkZMM0d1."
        actual = response_data.get('error')
        assert expected == actual

    def test_when_token_is_invalid(self):
        response = delete_an_order('v1u5bnEL_8qEBVhIfq3ze','ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58a')
        assert response.status_code == 401
        response_data = response.json()
        expected = "Invalid bearer token."
        actual = response_data.get('error')
        assert expected == actual


    def test_without_token(self):
        response = delete_an_order('v1u5bnEL_8qEBVhIfq3ze', '')
        assert response.status_code == 401
        response_data = response.json()
        expected = 'Invalid bearer token.'
        actual = response_data.get('error')
        assert expected == actual

    def test_when_order_id_and_token_are_invalid(self):
        response = delete_an_order('FYkZMM0d1kES5r5WZF0p','ba559cc80cdb0b484c663a28a33bfedbe85a2966636d108df528861030c58a')
        assert response.status_code == 401
        response_data = response.json()
        expected = "Invalid bearer token."
        actual = response_data.get('error')
        assert expected == actual



