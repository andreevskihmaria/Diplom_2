
#негативные данные для создания пользователя
class CreatedUser:

    #создание пользователя без почты
    user_wihtout_email = {
        'email': '',
        'password': 'qazwsx',
        'name': 'harry'
    }

    #создание пользователя без пароля
    user_wihtout_password = {
        'email': 'test@yandex.ru',
        'password': '',
        'name': 'harry'
    }

    #создание пользователя без имени
    user_wihtout_name = {
        'email': 'test@yandex.ru',
        'password': 'qazwsx',
        'name': ''
    }

#сообщения об ошибках при создании пользователя
class MessageError:

    #сообщение если не передать ни один ингредиент при создании заказа
    message_ingredient_ids_must_be_provided = 'Ingredient ids must be provided'

    #сообщение если нет одного из полей
    message_email_password_name_are_required_fields = 'Email, password and name are required fields'

    #сообщение если пользователь уже существует
    message_user_already_exists = 'User already exists'

    #сообщение об ошибке при авторизации с неверным логином или паролем
    message_email_or_password_are_incorrect = 'email or password are incorrect'

