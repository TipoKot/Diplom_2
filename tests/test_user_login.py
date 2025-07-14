import requests
import allure
import random
from data import BASE_URL

class TestUserLogin:
    @allure.title("Login with valid credentials")
    def test_login_existing_user(self, registered_user):
        login_payload = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = requests.post(f'{BASE_URL}/auth/login', json=login_payload)
        assert response.status_code == 200, "Expected status code 200 for successful login"
        assert response.json()["success"] is True, "Expected 'success' to be True in response"

    @allure.title("Login with invalid credentials")
    def test_login_wrong_user(self):
        payload = {
            "email": f"user{random.randint(1000, 9999)}@example.com",
            "password": "wrongpassword"
        }
        response = requests.post(f'{BASE_URL}/auth/login', json=payload)
        assert response.status_code == 401, "Expected status code 401 for unauthorized login"
        assert response.json()["success"] is False, "Expected 'success' to be False in response"