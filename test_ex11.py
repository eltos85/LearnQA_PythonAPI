import requests

def test_ex11():
    get_cookie = requests.get('https://playground.learnqa.ru/api/homework_cookie').cookies
    print(get_cookie.values())
    assert "hw_value" in get_cookie.values(), "Wrong values in cookies"