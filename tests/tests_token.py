from requests_folder.token_auth import get_token_data

class TestGetToken:

# acest test merge rulat o singura data, pentru ca se genereaza un token valabil 7 zile
# a 2-a ora vom primi un status code 400 si mesaj ca user este deja inregistrat
#     def test_when_user_is_not_registered(self):
#         response = get_token_data('alinatr444', 'alina454@example.com')
#         assert response.status_code == 201
#         assert bool(response.json().get('accessToken', False)) is True

    def test_when_user_is_registered(self):
        pass

    def test_when_name_is_a_number_and_email_valid(self):
        pass

    def test_when_name_is_a_special_char_and_email_valid(self):
        pass

    def test_when_name_is_valid_and_email_is_a_special_char(self):
        pass

    def test_when_name_is_valid_and_email_is_a_number(self):
        pass

    def test_when_both_name_and_email_are_special_chars(self):
        pass




