import time

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEditer(BaseCase):
    def test_edit_just_created_user(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        login_data = {
            'email': email,
            'password': password
            }
        response2 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        new_name = 'Changed Name'

        response3 = MyRequests.put(f"user/{user_id}",
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid},
                                 data={'firstName': new_name}
                                 )
        Assertions.assert_code_status(response3, 200)


        response4 = MyRequests.get(f"user/{user_id}",
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid}
                                 )
        Assertions.assert_json_value_by_name(response4, 'firstName', new_name, 'Wrong name of the user after edit')

    def test_no_auth_put_Ex17(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, 'id')

        new_name = 'Changed Name'
        response2 = MyRequests.put(f"user/{user_id}",
                                   data={'firstName': new_name}
                                   )
        Assertions.assert_code_status(response2, 400)

    def test_wrong_user_auth_Ex17(self):
        register_data1 = self.prepare_registration_data()
        response1 = MyRequests.post("user", data=register_data1)
        time.sleep(3)
        register_data2 = self.prepare_registration_data()
        response2 = MyRequests.post("user", data=register_data2)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        # One user
        email1 = register_data1['email']
        first_name1 = register_data1['firstName']
        password1 = register_data1['password']
        user_id1 = self.get_json_value(response1, 'id')
        login_data1 = {
            'email': email1,
            'password': password1
        }

        # Too user
        first_name2 = register_data2['firstName']
        user_id2 = self.get_json_value(response2, 'id')

        response3 = MyRequests.post("user/login", data=login_data1)

        auth_sid1 = self.get_cookie(response3, 'auth_sid')
        token1 = self.get_header(response3, 'x-csrf-token')
        new_name = 'Changed Name'

        response3 = MyRequests.put(f"user/{user_id2}",
                                 headers={'x-csrf-token': token1},
                                 cookies={'auth_sid': auth_sid1},
                                 data={'firstName': new_name}
                                 )
        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(f"user/{user_id1}",
                                   headers={'x-csrf-token': token1},
                                   cookies={'auth_sid': auth_sid1}
                                   )
        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_value_by_name(response4, 'firstName', first_name2, f'The firstName must be: {first_name2}')

    def test_edit_wrong_email_user_Ex17(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        login_data = {
            'email': email,
            'password': password
            }
        response2 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        email = 'testtest.ru'

        response3 = MyRequests.put(f"user/{user_id}",
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid},
                                 data={'email': email}
                                 )
        Assertions.assert_code_status(response3, 400)
        response4 = MyRequests.get(f"user/{user_id}",
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid}
                                 )
        Assertions.assert_json_value_by_name(response4, 'email', login_data['email'], 'Invalid email format')

    def test_edit_wrong_first_name_user_Ex17(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        first_name = 'y'

        response3 = MyRequests.put(f"user/{user_id}",
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid},
                                   data={'firstName': first_name}
                                   )
        Assertions.assert_code_status(response3, 400)
        response4 = MyRequests.get(f"user/{user_id}",
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid}
                                   )
        Assertions.assert_json_value_by_name(response4, 'first_name', login_data['firstName'],
                                             'Too short value for field firstName')