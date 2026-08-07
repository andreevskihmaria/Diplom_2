# API-автотесты Stellar Burgers

Автотесты REST API сервиса [Stellar Burgers](https://stellarburgers.education-services.ru) — регистрация и авторизация пользователей, создание заказов. По итогам тестирования найдены два дефекта, описанных в разделе [Результаты](#результаты).

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-8.x-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/requests-2.x-2C5BB4?style=flat-square)
![Allure](https://img.shields.io/badge/Allure-Report-FF6C37?style=flat-square)

---

## О проекте

Дипломный проект по автоматизации API-тестирования. Покрыты три группы ручек: создание пользователя, авторизация и создание заказа — в позитивных и негативных сценариях.

Ключевые решения:

- **Тесты не оставляют мусора.** Каждая фикстура создаёт пользователя со случайными данными и удаляет его после теста — прогон можно повторять сколько угодно раз, стенд не засоряется.
- **Работа с API вынесена из тестов.** Запросы живут в `api_methods/`, тесты содержат только сценарий и проверки. Смена эндпоинта не заставляет править тесты.
- **Никаких захардкоженных id.** Валидный `_id` ингредиента фикстура получает запросом к ручке ингредиентов и берёт случайный — тесты не ломаются при изменении данных на стенде.
- **Проверяется не только код ответа.** В негативных сценариях сверяется и текст сообщения об ошибке, в позитивных — структура тела ответа и наличие токенов.

## Что покрыто тестами

**Создание пользователя** — `tests/test_created_user.py`

| Тест | Ожидаемый результат |
|------|---------------------|
| `test_successful_user_creation` | `200`, `success: true`, в ответе есть `accessToken` и `refreshToken`, почта и имя совпадают с отправленными |
| `test_error_when_duplicating_user` | `403`, `User already exists` |
| `test_error_when_create_user_without_required_field` | `403`, `Email, password and name are required fields` — три случая: без почты, без пароля, без имени |

**Авторизация** — `tests/test_login_user.py`

| Тест | Ожидаемый результат |
|------|---------------------|
| `test_login_under_existing_user` | `200`, в ответе есть `accessToken` |
| `test_invalid_login_user` | `401`, `email or password are incorrect` — два случая: неверная почта, неверный пароль |

**Создание заказа** — `tests/test_create_order.py`

| Тест | Ожидаемый результат |
|------|---------------------|
| `test_creating_order_with_login` | `200` — заказ с ингредиентами и токеном |
| `test_creating_order_withot_ingredient` | `400`, `Ingredient ids must be provided` |
| `test_create_order_with_invalid_ingredient_hash` | `500` — невалидный хеш ингредиента |
| `test_creating_order_without_login` | `200` — заказ создаётся без токена |
| `test_creating_order_withot_ingredient_and_without_login` | `400`, `Ingredient ids must be provided` |
| `test_create_order_with_invalid_ingredient_and_without_login` | `500` |

Итого **11 тестовых функций**, которые с учётом параметризации дают **14 тест-кейсов**.

## Структура проекта

```text
.
├── api_methods/
│   ├── user_methods.py     # Создание, авторизация и удаление пользователя
│   └── order_methods.py    # Получение ингредиентов и создание заказа
├── tests/
│   ├── test_created_user.py
│   ├── test_login_user.py
│   └── test_create_order.py
├── conftest.py             # Фикстуры: генерация пользователя, токен, id ингредиента, очистка
├── data.py                 # Негативные наборы данных и ожидаемые тексты ошибок
├── helpers.py              # Генерация случайных почты, пароля и имени
├── urls.py                 # Базовый URL и эндпоинты
└── requirements.txt
```

## Требования

- Python 3.10 или новее
- Доступ в интернет — тесты работают с реальным учебным стендом
- Для просмотра отчётов — [Allure CLI](https://allurereport.org/docs/install/)

## Установка и запуск

```bash
git clone https://github.com/andreevskihmaria/stellar-burgers-api-tests.git
cd stellar-burgers-api-tests
python -m venv venv
```

Активировать окружение — Windows:

```bash
venv\Scripts\activate
```

macOS и Linux:

```bash
source venv/bin/activate
```

Установить зависимости и запустить тесты:

```bash
pip install -r requirements.txt
pytest -v
```

## Allure-отчёт

```bash
pytest --alluredir=allure_results
allure serve allure_results
```

Тесты размечены через `@allure.suite` и `@allure.title`, поэтому отчёт читается без обращения к коду.

## Результаты

Позитивные сценарии регистрации, авторизации и создания заказа работают корректно. Валидация обязательных полей и обработка неверных учётных данных соответствуют ожиданиям.

Найдены два отклонения от корректного поведения API:

**1. Заказ создаётся без авторизации**

`POST /api/orders` с валидным списком ингредиентов и **без** заголовка `Authorization` возвращает `200` и успешно создаёт заказ. Ожидаемое поведение — `401 Unauthorized`: заказ логически принадлежит пользователю, а созданный анонимно заказ не попадает в историю ни одного аккаунта.

Зафиксировано в `test_creating_order_without_login`.

**2. Невалидный хеш ингредиента приводит к `500`**

При передаче несуществующего хеша ингредиента (например, `'1234342'`) сервер отвечает `500 Internal Server Error` — и с авторизацией, и без неё. Ожидаемое поведение — `400 Bad Request` с внятным сообщением. Код `500` означает, что запрос не валидируется, а роняет обработчик.

Зафиксировано в `test_create_order_with_invalid_ingredient_hash` и `test_create_order_with_invalid_ingredient_and_without_login`.

Оба теста намеренно закрепляют **фактическое** поведение сервиса, а не желаемое: так тест остаётся зелёным на текущей версии и покраснеет, когда поведение исправят. Ожидаемые по спецификации коды описаны здесь, в документации.

## Автор

Мария Андреевских — [GitHub](https://github.com/andreevskihmaria)

Проект выполнен в рамках дипломной работы курса «Инженер по автоматизации тестирования на Python» Яндекс Практикума.
