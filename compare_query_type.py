import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
esy_get = requests.get(url)
head_request = requests.head(url)
get_request = requests.get(url, params={"method":"GET"})
post_request = requests.post(url, data={"method":"POST"})
put_request = requests.put(url, data={"method":"PUT"})
del_request = requests.delete(url, data={"method":"DELETE"})


print("esy get: ", esy_get,
      "\nesy get text: ", esy_get.text)
print("head request: ", head_request,
      "\nhead request text: ", head_request.text)
print("perfect get: ", get_request,
      "\nperfect get text: ", get_request.text )

requests_dick = ["GET", "POST", "PUT", "DELETE"]

for i in requests_dick:
    print(f"GET: {i}", requests.get(url, params={"method": f"{i}"}).text)
    print(f"POST: {i}", requests.post(url, data={"method": f"{i}"}).text)
    print(f"PUT: {i}", requests.put(url, data={"method": f"{i}"}).text)
    print(f"DELETE: {i}", requests.delete(url, data={"method": f"{i}"}).text)



print(post_request.text)
print(put_request.text)
print(del_request.text)