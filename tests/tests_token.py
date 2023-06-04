from requests_folder.token_auth import get_token_data

class TestGetToken:

    def test_get_token_when_user_is_not_registered(self):
        response = get_token_data('alinatr444', 'alina454@example.com')
        assert response.status_code == 201
        assert bool(response.json().get('accessToken', False)) is True

    def test_get_token_when_user_is_registered(self):
        pass
