import pytest
from helpers import generate_user_payload
from api_methods.user_methods import UserMothod




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


@pytest.fixture #создание пользователя, передача в тест, авторизация и ладение пользователя
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
        


