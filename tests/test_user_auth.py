
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserAuth(BaseCase):
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post('user/login', data=data)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        response2 = MyRequests.get(f"user/{user_id_from_auth_method}",
                                 headers={'x-csrf-token': token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    def test_get_user_Ex16(self):
        data1 = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        data2 = {
            'email': 'learnqa07072022174915@example.com',
            'password': '123'
        }

        response1 = MyRequests.post("user/login", data=data1)
        auth_sid1 = self.get_cookie(response1, 'auth_sid')
        token1 = self.get_header(response1, 'x-csrf-token')
        response2 = MyRequests.post("user/login", data=data2)
        auth_sid2 = self.get_cookie(response2, 'auth_sid')
        token2 = self.get_header(response2, 'x-csrf-token')
        response3 = MyRequests.get(f"user/{self.get_json_value(response1, 'user_id')}",
                                 headers={'x-csrf-token': token2},
                                 cookies={"auth_sid": auth_sid2}
                                 )
        Assertions.assert_json_has_key(response3, 'username')
