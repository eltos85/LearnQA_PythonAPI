import time
import json

import requests

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

get_request = requests.get(url)
token = {"token": get_request.json()['token']}
get_request_token = requests.get(url, params=token)
status = json.loads(get_request_token.text)
try:
    assert status['status'] == 'Job is NOT ready', 'wrong status'
    time.sleep(get_request.json()['seconds'])
    get_request_token_new_status = requests.get(url, params=token).json()
    assert get_request_token_new_status['status'] == 'Job is ready', 'wrong status'
    assert get_request_token_new_status['result'], 'result not found'
except AssertionError as e:
    print(e)