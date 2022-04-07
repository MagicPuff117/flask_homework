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



resp3 = requests.delete(f'{HOST}/delete_ad/1')


print(resp3.status_code)
print(resp3.text)