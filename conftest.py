import pytest
import json
import requests
from halper import Halper
from data import URL, OrderData


@pytest.fixture(scope='function')
def generate_courier_data_and_delete_courier():
    payload = {
        "login": Halper.generate_random_string(10),
        "password": Halper.generate_random_string(10),
        "firstName": Halper.generate_random_string(10)
    }
    yield payload
    if "firstName" in payload.keys():
        del payload["firstName"]
    response_login = requests.post(f'{URL}/api/v1/courier/login', data=payload)
    courier_id = response_login.json()['id']
    requests.delete(f'{URL}/api/v1/courier/{courier_id}')


@pytest.fixture(scope='function')
def creation_courier_and_delete_courier(generate_courier_data_and_delete_courier):
    payload = generate_courier_data_and_delete_courier
    requests.post(f'{URL}/api/v1/courier', data=generate_courier_data_and_delete_courier)
    if "firstName" in payload.keys():
        del payload["firstName"]
    return payload


@pytest.fixture(scope='function')
def create_order_and_cancel_order():
    payload = json.dumps(OrderData.base_order_data)
    response = requests.post(f'{URL}/api/v1/orders', data=payload)
    yield response.json()
    requests.put(f'{URL}/api/v1/orders/cancel', data=response.json())
