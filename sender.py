import requests

url = 'https://992876609b4d.ngrok.io'
#http://127.0.0.1:5000/send

name = input('Введи имя: ')
while True:
    text = input()
    data = {'name': name, 'text': text}
    response = requests.post(url, json=data)
