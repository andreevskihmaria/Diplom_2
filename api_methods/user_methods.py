import requests
import allure
from urls import URLS

class UserMothod:

    
    @staticmethod
    @allure.step("Создать пользователя")
    def create_user(payload):
        return requests.post(URLS.CREATE_USER_ENDPOINT, json=payload)

    
    @staticmethod
    @allure.step("Авторизоваться")
    def login_user(payload):
        return requests.post(URLS.LOGIN_USER_ENDPOINT, json=payload)

    
    @staticmethod
    @allure.step("Удалить пользователя)")
    def delete_user(user_token):
        headers = {
            'Authorization': user_token
        }
        return requests.delete(URLS.DELETE_USER_ENDPOINT, headers=headers)
