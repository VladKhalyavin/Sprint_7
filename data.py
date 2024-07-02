from halper import Halper

URL = 'http://qa-scooter.praktikum-services.ru'


class CourierData:
    # Тестовые наборы для создания курьера
    body_without_required_field = [{"login": Halper.generate_random_string(10)},
                                   {"password": Halper.generate_random_string(10)},
                                   {"login": Halper.generate_random_string(10),
                                    "password": ""},
                                   {"login": "",
                                    "password": Halper.generate_random_string(10)}]

    # Ответы на запросы создания курьера
    successful_creation_result = {'ok': True}
    creation_existing_login_result = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."
    }
    creation_with_body_without_required_field = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"
    }

    # Тестовые наборы для авторизации курьера
    body_non_existent_courier = {"login": "Halper.generate_random_string(10)",
                                 "password": Halper.generate_random_string(10)}

    # Ответы на запросы авторизации курьера

    authorization_with_body_without_required_field = {
        "code": 400,
        "message": "Недостаточно данных для входа"
    }
    authorization_non_existent_courier = {
        "code": 404,
        "message": "Учетная запись не найдена"
    }


class OrderData:

    # Тестовые наборы для создания курьера

    base_order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

    scooter_colors = [["BLACK"], ["GRAY"], ["BLACK", "GRAY"], []]

    fields_order_response = ["id", "courierId", "firstName", "lastName", "address", "metroStation", "phone", "rentTime",
                             "deliveryDate", "track", "color", "comment", "createdAt", "updatedAt", "status"]
