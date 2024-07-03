import requests
import json
import pytest
import allure
from data import URL, OrderData


class TestCreationCourier:
    """
    Проверки создания заказа
    """
    orders_numbers = []

    @pytest.mark.parametrize('color', OrderData.scooter_colors)
    @allure.title('Создание заказа с различной конфигурацией цветов самокатов - заказ создан успешно')
    def test_create_order_with_difficult_scooter_color_successful(self, color):
        OrderData.base_order_data["color"] = color
        payload = json.dumps(OrderData.base_order_data)
        response = requests.post(f'{URL}/api/v1/orders', data=payload)
        self.orders_numbers.append(response.json())
        assert response.status_code == 201 and "track" in response.json()

    @classmethod
    def teardown_class(cls):
        for i in cls.orders_numbers:
            requests.put(f'{URL}/api/v1/orders/cancel', data=i)


class TestGetOrdersList:
    """
    Проверка получения списка заказов
    """

    @allure.title('Получение списка заказов - успешное получение списка заказов')
    def test_get_orders_list_successful(self, create_order_and_cancel_order):
        response = requests.get(f'{URL}/api/v1/orders')
        assert (response.status_code == 200
                and "orders" in response.json()
                and len(response.json()["orders"]) >= 1
                and OrderData.fields_order_response == list(response.json()["orders"][0].keys()))

