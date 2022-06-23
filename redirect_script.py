import requests

get_request = requests.get("https://playground.learnqa.ru/api/long_redirect")

his = get_request.history
print(get_request)
print("count history gets: ", len(his))