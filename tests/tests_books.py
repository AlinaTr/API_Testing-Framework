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
        pass

    def test_with_limit_is_1(self):
        pass

    def test_with_limit_is_20(self):
        pass

    def test_with_limit_positive_and_lower_than_accepted_range(self):
        pass

    def test_with_limit_greater_than_accepted_range(self):
        pass

    def test_with_limit_negative(self):
        response = get_all_books(limit= -2)
        assert response.status_code == 400
        assert response.json().get('error', '') == "Invalid value for query parameter 'limit'. Must be greater than 0."

    def test_with_limit_is_special_char(self):
        pass


class TestGetBookById():

    def test_when_book_is_valid_and_book_exists_in_db(self):
        response = get_book_by_id(2)
        assert response.status_code == 200
        assert response.json()

    def test_when_book_id_is_valid_and_book_does_not_exist_in_db(self):
        pass

    def test_when_book_id_is_a_negative_number(self):
        pass

    def test_when_book_id_is_a_letter(self):
        pass

    def test_when_book_id_is_special_char(self):
        pass




