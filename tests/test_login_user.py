from api_methods.user_methods import UserMothod
import pytest
import allure


@allure.suite('Авторизация пользователя')
class TestLoginUser:


    @allure.title('Успешный вход существующего пользователя')
    def test_login_under_existing_user(self, created_user):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"]
        }
        response = UserMothod.login_user(payload)

        assert response.status_code == 200
        assert 'accessToken' in response.json()


    @allure.title('Ошибка авторизации с неверным логином или паролем')
    @pytest.mark.parametrize('field, incorrect_value', [
        ("email", "incorrect_email@yandex.ru"),
        ("password", "incorrect")
    ])
    def test_invalid_login_user(self, created_user, field, incorrect_value):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"]
        }

        payload[field] = incorrect_value

        response = UserMothod.login_user(payload)

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'
        