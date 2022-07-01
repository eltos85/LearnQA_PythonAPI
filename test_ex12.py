import requests

def test_ex12():
    request_headers = requests.get("https://playground.learnqa.ru/api/homework_header").headers
    headers_key = ['Date', 'Content-Type', 'Content-Length', 'Connection', 'Keep-Alive', 'Server', 'x-secret-homework-header', 'Cache-Control', 'Expires']

    for i in headers_key:
        assert i in request_headers.keys(), "Key not found in cookies header"


