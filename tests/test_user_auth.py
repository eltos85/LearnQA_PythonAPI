
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserAuth(BaseCase):

    def test_auth_user_from_Ex16(self):
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
