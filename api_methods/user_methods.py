import requests
from urls import URLS

class UserMothod:

    #создание пользователя
    @staticmethod
    def create_user(payload):
        return requests.post(URLS.CREATE_USER_ENDPOINT, data=payload)

    #авторизация пользователя
    @staticmethod
    def login_user(payload):
        return requests.post(URLS.LOGIN_USER_ENDPOINT, data=payload)

    #укдаление пользователя
    @staticmethod
    def delete_user(user_token):
        return requests.delete(f'{URLS.DELETE_USER_ENDPOINT}{user_token}')
