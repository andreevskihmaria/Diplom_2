import requests
import allure
from urls import URLS



class OrderMethod:


    @staticmethod
    @allure.step("Получить данные об ингредиентах")
    def get_info_order():
        return requests.get(URLS.GET_INFO_INGREDIENTS_ENDPOINT)


    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload, access_token=None):
        if access_token:
            headers = {
                "Authorization": access_token
            }
            return requests. post(URLS.CREATE_ORDER_ENDPOINT, json=payload, headers=headers)
        
        return requests.post(URLS.CREATE_ORDER_ENDPOINT, json=payload)
