import requests
import allure
import random
from data import BASE_URL
from response_messages import ERROR_REQUIRED_FIELDS

class TestUserRegistration:
    @allure.title("Тестирование регистрации пользователя")
    def test_create_user(self):
        payload = {
            "email": f"user{random.randint(1000, 9999)}@example.com",
            "password": "password123",
            "name": "Test User"
        }
        response = requests.post(f'{BASE_URL}/auth/register', json=payload)
        assert response.status_code == 200, "Expected status code 200 for successful user registration"
        assert response.json()["success"] is True, "Expected 'success' to be True in response"

    @allure.title("Тестирование регистрации дублирующегося пользователя")
    def test_create_duplicate_user(self):
        payload = {
            "email": f"user{random.randint(1000, 9999)}@example.com",
            "password": "password123",
            "name": "Test User"
        }
        requests.post(f'{BASE_URL}/auth/register', json=payload)
        response = requests.post(f'{BASE_URL}/auth/register', json=payload)
        assert response.status_code == 403, "Expected status code 403 for duplicate user registration"
        assert response.json()["success"] is False, "Expected 'success' to be False in response"

    @allure.title("Тестирование регистрации пользователя без обязательного поля")
    def test_create_user_without_required_field(self):
        payload = {
            "email": "",
            "password": "password123",
            "name": "Test User"
        }
        response = requests.post(f'{BASE_URL}/auth/register', json=payload)
        assert response.status_code == 403, "Expected status code 403 for missing required field"
        assert response.json()["success"] is False, "Expected False for 'success' in response"
        assert response.json()["message"] == ERROR_REQUIRED_FIELDS, "Expected specific error message for missing required field"