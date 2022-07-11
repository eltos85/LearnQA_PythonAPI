import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("user", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_exesting_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"User with email '{email}' already exist", \
            f"Unexpected response content {response.content}"

    def test_create_user_with_wrong_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", \
            f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('param', ['email', 'password', 'username', 'firstName', 'lastName'])
    def test_create_user_with_wrong_data(self, param):
        data = self.get_params(param)
        response = MyRequests.post("user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {param}", \
            f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('lens', [1, 250])
    def test_create_user_by_name_length(self, lens):
        data = self.get_random_name(lens)
        response = MyRequests.post("user", data=data)
        if lens == 1:
            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The value of 'username' field is too short", \
                f"Lens name {lens}"
        else:
            Assertions.assert_code_status(response, 200)
            Assertions.assert_json_has_not_key(response, "id")
