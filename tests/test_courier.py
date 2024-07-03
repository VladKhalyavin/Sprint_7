import requests
import pytest
import allure
from data import URL, CourierData
from halper import Halper


class TestCreationCourier:
    """
    Проверки создания курьера
    """

    @allure.title('Создание курьера - курьер создан успешно')
    def test_create_courier_successful(self, generate_courier_data_and_delete_courier):
        response = requests.post(f'{URL}/api/v1/courier', data=generate_courier_data_and_delete_courier)
        assert response.status_code == 201 and response.json() == CourierData.successful_creation_result

    @allure.title('Создание курьера с существующим логином - получено сообщение об ошибке')
    def test_create_courier_existing_login_creation_error(self, generate_courier_data_and_delete_courier):
        requests.post(f'{URL}/api/v1/courier', data=generate_courier_data_and_delete_courier)
        response = requests.post(f'{URL}/api/v1/courier', data=generate_courier_data_and_delete_courier)
        assert response.status_code == 409 and response.json() == CourierData.creation_existing_login_result

    @allure.title('Cоздание курьера без обязательных полей в запросе - получено сообщение об ошибке')
    @pytest.mark.parametrize('payload', CourierData.body_without_required_field)
    def test_create_body_without_required_field_creation_error(self, payload):
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        assert response.status_code == 400 and response.json() == CourierData.creation_with_body_without_required_field


class TestLoginCourier:
    """
    Проверки авторизации курьера
    """
    @allure.title('Авторизация курьера - курьер успешно авторизован')
    def test_authorization_courier_successful(self, creation_courier_and_delete_courier):
        response = requests.post(f'{URL}/api/v1/courier/login', data=creation_courier_and_delete_courier)
        courier_id = response.json()['id']
        assert response.status_code == 200 and response.json() == {'id': courier_id}

    @allure.title('Авторизация курьера без обязательных полей в запросе - получено сообщение об ошибке')
    @pytest.mark.parametrize('payload', CourierData.body_without_required_field)
    def test_authorization_body_without_required_field_authorization_error(self, payload):
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert (response.status_code == 400
                and response.json() == CourierData.authorization_with_body_without_required_field)

    @allure.title('Авторизация курьера с несуществующими данными УЗ - получено сообщение об ошибке')
    def test_authorization_non_existent_courier_authorization_error(self):
        response = requests.post(f'{URL}/api/v1/courier/login', data=CourierData.body_non_existent_courier)
        assert response.status_code == 404 and response.json() == CourierData.authorization_non_existent_courier

    @allure.title('Авторизация курьера с невалидными логином - получено сообщение об ошибке')
    def test_authorization_invalid_login_authorization_error(self, creation_courier_and_delete_courier):
        payload = creation_courier_and_delete_courier.copy()
        payload["login"] += f'{Halper.generate_random_string(1)}'
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert response.status_code == 404 and response.json() == CourierData.authorization_non_existent_courier

    @allure.title('Авторизация курьера с неполным паролем - получено сообщение об ошибке')
    def test_authorization_invalid_password_authorization_error(self, creation_courier_and_delete_courier):
        payload1 = creation_courier_and_delete_courier.copy()
        payload1["password"] = payload1["password"][:-1]
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload1)
        assert response.status_code == 404 and response.json() == CourierData.authorization_non_existent_courier


