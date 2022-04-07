import requests
import datetime as dt
from flask import jsonify

HOST = 'http://127.0.0.1:8080'


resp1 = requests.post(f'{HOST}/new_user', json={
    'header': 'HELLO',
    'description': 'HELLO',
    'date': None
})


resp2 = requests.get(f'{HOST}/get_ad/2')


print(resp2.status_code)
print(resp2.text)