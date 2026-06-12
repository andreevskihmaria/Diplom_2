from api_methods.order_methods import OrderMethod
import allure
from data import MessageError


@allure.suite('Создание заказа с авторизацией')
class TestCreatedOrderWithLogin:

    @allure.title('Создание заказа с ингредиентами и авторизацией')
    def test_creating_order_with_login(self, access_token, ingredient_id):
        payload = {
            "ingredients": [ingredient_id]
        }

        response = OrderMethod.create_order(payload, access_token)

        assert response.status_code == 200

    
    @allure.title('Создание заказа без ингредиентов и с авторизацией')
    def test_creating_order_withot_ingredient(self, access_token):
       payload = {
          "ingredients": []
          } 
       response = OrderMethod.create_order(payload, access_token)

       assert response.status_code == 400
       assert response.json()['message'] == MessageError.message_ingredient_ids_must_be_provided


    @allure.title('Создание заказа с невалидным хешем ингредиента и авторизацией')
    def test_create_order_with_invalid_ingredient_hash(self, access_token):
       payload = {
          "ingredients": ['1234342']
       }
       
       response = OrderMethod.create_order(payload, access_token)

       assert response.status_code == 500
   
      
@allure.suite('Создание заказа без авторизации')
class TestCreatedOrderWithutLogin:

     
    @allure.title('Создание заказа с ингредиентами без авторизации')
    def test_creating_order_without_login(self, ingredient_id):
     payload = {
        "ingredients": [ingredient_id]
     }

     response = OrderMethod.create_order(payload)

     assert response.status_code == 200


    @allure.title('Создание заказа без ингредиентов и без авторизации')
    def test_creating_order_withot_ingredient_and_without_login(self):
       payload = {
          "ingredients": []
       }

       response = OrderMethod.create_order(payload)

       assert response.status_code == 400
       assert response.json()['message'] == MessageError.message_ingredient_ids_must_be_provided


    @allure.title('Создание заказа с невалидным хешем ингредиента без авторизации')
    def test_create_order_with_invalid_ingredient_and_without_login(self):
       payload = {
          "ingredients": ['124512']
       }

       response = OrderMethod.create_order(payload)

       assert response.status_code == 500
