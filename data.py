
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
    