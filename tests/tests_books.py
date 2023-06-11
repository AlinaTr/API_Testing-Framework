from requests_folder.books import get_all_books, get_book_by_id

class TestGetAllBooks:

    def test_with_no_filters_applied(self):
        response = get_all_books()
        assert response.status_code == 200
        assert len(response.json()) == 6

    def test_with_type_is_fiction(self):
        response = get_all_books(type = 'fiction')
        assert response.status_code == 200
        assert len(response.json()) == 4

    def test_with_type_is_non_fiction(self):
        response = get_all_books(type='non-fiction')
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_with_type_is_valid_type_but_not_accepted(self):
        response = get_all_books(type='romance')
        assert response.status_code == 400
        response_data = response.json()
        expected = "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."
        actual = response_data.get("error", "")
        assert expected == actual
        # sau
        # assert response_data.get('error', '') == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_with_type_is_not_valid(self):
        response = get_all_books('@#%ufh')
        assert response.status_code == 400
        response_data = response.json()
        expected = "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."
        actual = response_data.get('error', '')
        assert expected == actual

    def test_with_limit_is_between_accepted_range(self):
        # limit is between 1-20
        response = get_all_books(limit=2)
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_with_limit_is_1(self):
        response = get_all_books(limit = 1)
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_with_limit_is_20(self):
        response = get_all_books(limit=20)
        assert response.status_code == 200
        assert len(response.json()) == 6

    def test_with_limit_positive_and_lower_than_accepted_range(self):
        response = get_all_books(limit=0)
        assert response.status_code == 200
        assert len(response.json())

    """
    Tests bug reports:
    Get all books nu functioneaza corespunzator atunci cand limita este un 0
    => vezi test test_with_limit_positive_and_lower_than_accepted_range
    """

    def test_with_limit_greater_than_accepted_range(self):
        response = get_all_books(limit=25)
        assert response.status_code == 400
        response_data = response.json()
        expected = "Invalid value for query parameter 'limit'. Cannot be greater than 20."
        actual = response_data.get('error', '')
        assert expected == actual


    def test_with_limit_negative(self):
        response = get_all_books(limit= -2)
        assert response.status_code == 400
        assert response.json().get('error', '') == "Invalid value for query parameter 'limit'. Must be greater than 0."

    def test_with_limit_is_special_char(self):
        response = get_all_books(limit='@')
        assert response.status_code == 200
        assert len(response.json())

    """
    Tests bug reports:
    Get all books nu functioneaza corespunzator atunci cand limita este un caracter special
    => vezi test test_with_limit_is_special_char
    """

    def test_when_type_is_accepted_and_limit_between_accepted_range(self):
        pass

    def test_when_type_is_not_accepted_and_limit_outside_accepted_range(self):
        pass

    def test_when_type_is_valid_type_but_not_accepted_and_limit_between_accepted_range(self):
        pass

    def test_when_type_is_not_valid_and_limit_between_accepted_range(self):
        pass





class TestGetBookById:

    def test_when_book_is_valid_and_book_exists_in_db(self):
        response = get_book_by_id(2)
        assert response.status_code == 200
        assert response.json()

    def test_when_book_id_is_valid_and_book_does_not_exist_in_db(self):
        response = get_book_by_id(7)
        assert response.status_code == 404
        response_data = response.json()
        expected = "No book with id 7"
        actual = response_data.get('error' '')
        assert expected == actual

    def test_when_book_id_is_a_negative_number(self):
        response = get_book_by_id(-5)
        assert response.status_code == 404
        response_data = response.json()
        expected = "No book with id -5"
        actual = response_data.get('error' '')
        assert expected == actual

    def test_when_book_id_is_a_letter(self):
        response = get_book_by_id('p')
        assert response.status_code == 404
        response_data = response.json()
        expected = "No book with id NaN"
        actual = response_data.get('error')
        assert expected == actual

    def test_when_book_id_is_special_char(self):
        response = get_book_by_id('@')
        assert response.status_code == 404
        response_data = response.json()
        expected = "No book with id NaN"
        actual = response_data.get('error')
        assert expected == actual




