class URLS:

    BASE_URL = 'https://stellarburgers.education-services.ru'
    CREATE_USER_ENDPOINT = f'{BASE_URL}/api/auth/register' #создание пользователя
    LOGIN_USER_ENDPOINT = f'{BASE_URL}/api/auth/login' #авторизация пользователя
    CREATE_ORDER_ENDPOINT = f'{BASE_URL}/api/orders' #создание заказа
    DELETE_USER_ENDPOINT = f'{BASE_URL}/api/auth/user' #удаление пользователя