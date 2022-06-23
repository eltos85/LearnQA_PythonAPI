import requests

def get_too_welloworld():
    payload = {"name": "User"}
    response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
    print(response.json()["answer"])


get_too_welloworld()