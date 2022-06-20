import requests

def get_too_welloworld():
    print(requests.get('https://playground.learnqa.ru/api/get_text').content)


get_too_welloworld()