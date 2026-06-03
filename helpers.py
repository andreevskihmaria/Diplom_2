import random
import string


#генерация рандомных данных для регистрации пользователя
def generate_user_payload():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload
