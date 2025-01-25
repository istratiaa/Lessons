from faker import Faker
import pytest
import requests

from tests.constant import HEADERS
from tests.constant import BASE_URL

fake = Faker()


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture(scope="session")
def booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": fake.text(max_nb_chars=fake.random_int(min=10, max=50))
    }


@pytest.fixture(scope="session")
def put_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": fake.text(max_nb_chars=fake.random_int(min=10, max=50))
    }


@pytest.fixture(scope="session")
def put_negative_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": fake.text(max_nb_chars=fake.random_int(min=10, max=50))
    }


@pytest.fixture(scope="session")
def patch_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000)

    }


@pytest.fixture(scope="session")
def booking_id(auth_session, booking_data):
    create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert create_booking.status_code == 200
    booking_id = create_booking.json().get("bookingid")
    assert booking_id is not None, "ID букинга не найден в ответе"

    get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_booking.status_code == 200

    booking_data_response = get_booking.json()
    assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
    assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
    assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
    assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
    assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
        'checkin'], "Дата заезда не совпадает"
    assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
        'checkout'], "Дата выезда не совпадает"
    return booking_id
