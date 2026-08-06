import pytest
import random
from helpers import generate_user_payload
from api_methods.user_methods import UserMothod
from api_methods.order_methods import OrderMethod


@pytest.fixture #геренерация данных и передача в тест, авторизация и удаление пользователя
def user_payload():
    payload = generate_user_payload()

    yield payload

    login_payload = {
        "email": payload['email'],
        "password": payload['password']
    }
    login_response = UserMothod.login_user(login_payload)
     
    if login_response.status_code == 200:
        user_token = login_response.json()['accessToken']
        UserMothod.delete_user(user_token)


@pytest.fixture #создание пользователя, передача в тест, авторизация и удаление пользователя
def created_user():
    payload = generate_user_payload()
    UserMothod.create_user(payload)

    yield payload

    login_payload = {
        "email": payload['email'],
        "password": payload['password']
    }
    login_response = UserMothod.login_user(login_payload)
     
    if login_response.status_code == 200:
        user_token = login_response.json()['accessToken']
        UserMothod.delete_user(user_token)
        

#получить id ингредиента
@pytest.fixture
def ingredient_id():
    response = OrderMethod.get_info_order()
    body = response.json()
    ingredient = random.choice(body['data'])
    return ingredient['_id']


@pytest.fixture #получение токена авторизации
def access_token(created_user):
    login_payload = {
        "email": created_user['email'],
        "password": created_user['password']
    }
    login_response = UserMothod.login_user(login_payload)

    return login_response.json()["accessToken"]
