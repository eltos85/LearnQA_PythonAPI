from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):
    def test_delete_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.post("user/login", data=data)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')
        user_id = self.get_json_value(response, 'user_id')
        response2 = MyRequests.delete(f'user/{user_id}',
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid},
                                      data=data
                                        )
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_error_message(response2, 'Please, do not delete test users ')

    def test_reg_and_delete_user(self):
        # registration
        data = self.prepare_registration_data()
        response = MyRequests.post("user", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        #auth

        response = MyRequests.post("user/login", data=data)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')
        user_id = self.get_json_value(response, 'user_id')

        #delete

        response2 = MyRequests.delete(f'user/{user_id}',
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid},
                                      data=data
                                      )
        Assertions.assert_code_status(response2, 200)

        response3 = MyRequests.post("user/login", data=data)
        Assertions.assert_code_status(response3, 400)
        Assertions.assert_error_message(response3, 'Invalid username/password supplied')

    def test_delete_user_wrong_auth(self):


        # auth user 1
        data = self.prepare_registration_data()
        response5 = MyRequests.post("user", data=data)
        response = MyRequests.post("user/login", data=data)
        print(response.content)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')
        user_id = self.get_json_value(response, 'user_id')

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "user_id")
        Assertions.assert_code_status(response5, 200)
        Assertions.assert_json_has_key(response5, "id")


        # auth user 2
        data2 = self.prepare_registration_data()
        response2 = MyRequests.post("user", data=data2)
        response3 = MyRequests.post("user/login", data=data)
        user_id2 = self.get_json_value(response3, 'user_id')
        token2 = self.get_header(response3, 'x-csrf-token')

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "user_id")

        # rty delete user

        response4 = MyRequests.delete(f'user/{user_id2}',
                                              headers={'x-csrf-token': token2},
                                              cookies={'auth_sid': auth_sid},
                                              data=data
                                              )
        Assertions.assert_code_status(response4, 400)
        Assertions.assert_error_message(response4, 'Please, do not try delete users ')
