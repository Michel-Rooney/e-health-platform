import requests


DOMINIO = 'http://192.168.3.11:8000/'
PATH = 'arduino/heart_rate/?'
CODE = 'code=316fc6ec40511933dc2c232a470144b24a18f22e5d26d5901b4f311b1e4da84b'
BEAT = '&beat=10'

lista = [1, 1, 2, 3, 5, 2, 1, 1, 1, 1]

for i in lista:
    BEAT = f'&beat={i}'
    url = DOMINIO + PATH + CODE + BEAT
    response = requests.get(url)

    print(response.content)