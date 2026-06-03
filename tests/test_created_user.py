from api_methods.user_methods import UserMothod
import pytest
from data import CreatedUser

#создание пользователя
class TestCreateUser:

    #создание уникального пользователя
    def test_successful_user_creation(self, user_payload):
        response = UserMothod.create_user(user_payload)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['success'] is True
        assert response_body['user']['email'] == user_payload['email']
        assert response_body['user']['name'] == user_payload['name']
        assert 'accessToken' in response_body
        assert 'refreshToken' in response_body

    
    #создание существующего пользователя
    def test_error_when_duplicating_user(self, user_payload):
        UserMothod.create_user(user_payload)

        response = UserMothod.create_user(user_payload)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'


    #ошибка при отсутствии обязазельного поля
    @pytest.mark.parametrize('payload', [
        CreatedUser.user_wihtout_email,
        CreatedUser.user_wihtout_password,
        CreatedUser.user_wihtout_name
        ])
    def test_error_when_create_user_without_required_field(self, payload):
        response = UserMothod.create_user(payload)

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
        