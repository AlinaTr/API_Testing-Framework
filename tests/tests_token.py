from requests_folder.token_auth import get_token_data

class TestGetToken:

# acest test merge rulat o singura data, pentru ca se genereaza un token valabil 7 zile
# a 2-a ora vom primi un status code 400 si mesaj ca user este deja inregistrat
#     def test_when_user_is_not_registered(self):
#         response = get_token_data('alinatr444', 'alina454@example.com')
#         assert response.status_code == 201
#         assert bool(response.json().get('accessToken', False)) is True

    def test_when_user_is_registered(self):
        response = get_token_data('alinatr444', 'alina454@example.com')
        assert response.status_code == 409
        response_data = response.json()
        expected = "API client already registered. Try a different email."
        actual = response_data.get('error', '')
        assert actual == expected


    # def test_when_name_is_a_number_and_email_valid(self):
    #     response = get_token_data(7, 'alina119@example.com')
    #     assert response.status_code == 201
    #     assert response.json()

    """ Tests bug reports:
    get_token_data nu functioneaza corespunzator cand ia ca paramtru un numar in loc de client_name(string)
    => vezi test_when_name_is_a_number_and_email_valid
    - Acest test merge rulat o singura data, a 2-a oara va da eroare, 
    pentru ca se genereaza token 
    
    """
    def test_when_name_is_a_special_char_and_email_valid(self):
        response = get_token_data('#', 'alina500@example.com')
        assert response.status_code == 400
        response_data = response.json()
        expected = 'Invalid or missing client name.'
        actual = response_data.get('error', '..........')
        assert expected == actual


    def test_when_name_is_valid_and_email_is_a_special_char(self):
        response = get_token_data('alina500', '#')
        assert response.status_code == 400
        response_data = response.json()
        expected = 'Invalid or missing client email.'
        actual = response_data.get('error', '...............')
        assert expected == actual

    def test_when_name_is_valid_and_email_is_a_number(self):
        response = get_token_data('alina500', 3)
        assert response.status_code == 400
        response_data = response.json()
        expected = 'Invalid or missing client email.'
        actual = response_data.get('error', '.........')
        assert expected == actual

    def test_when_both_name_and_email_are_special_chars(self):
        response = get_token_data('#', "#")
        assert response.status_code == 400
        response_data = response.json()
        expected = 'Invalid or missing client name.'
        actual = response_data.get('error', '.........')
        assert expected == actual

    def test_when_both_name_and_email_are_numbers(self):
        response = get_token_data(5, 7)
        assert response.status_code == 400
        response_data = response.json()
        expected = 'Invalid or missing client email.'
        actual = response_data.get('error', '.........')
        assert expected == actual








