import requests


DOMINIO = 'http://127.0.0.1:8000/'
PATH = 'arduino/heart_rate/?'
CODE = 'code=76ef51c95ce8579f9db39612b91a7e26b955245dc8936f114ef74ce680e63d78'
BEAT = '&beat=10'

lista = [1, 1, 2, 3, 5, 2, 1, 1, 1, 1]

for i in lista:
    BEAT = f'&beat={i}'
    url = DOMINIO + PATH + CODE + BEAT
    response = requests.get(url)

    print(response.content)
