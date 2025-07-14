import requests
import allure
import random
from data import BASE_URL
from response_messages import ERROR_UNAUTHORIZED

class TestUserDataChange:
    # Для обеих ситуаций нужно проверить, что любое поле можно изменить. Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
    #с авторизацией
    @allure.title("Change user data with authorization")
    def test_change_user_data_with_auth(self, registered_user):
        new_name = "Updated User"
        new_email = f"user{random.randint(1000, 9999)}@example_08.com"
        payload = {
            "name": new_name,
            "email": new_email
        }
        response = requests.patch(f'{BASE_URL}/auth/user', json=payload, headers=registered_user["headers"])
        assert response.status_code == 200, "Expected status code 200 for successful user data change"
        assert response.json()["success"] is True, "Expected 'success' to be True in response"
        assert response.json()["user"]["name"] == new_name, "Expected user name to be updated"
        assert response.json()["user"]["email"] == new_email, "Expected user email to be updated"

    # без авторизации
    @allure.title("Change user data without authorization")
    def test_change_user_data_without_auth(self):
        new_name = "Updated User"
        new_email = f"user{random.randint(1000, 9999)}@example_08.com"
        payload = {
            "name": new_name,
            "email": new_email
        }
        response = requests.patch(f'{BASE_URL}/auth/user', json=payload)
        assert response.status_code == 401, "Expected status code 401 for unauthorized user data change"
        assert response.json()["success"] is False, "Expected 'success' to be False in response"
        assert response.json()["message"] == ERROR_UNAUTHORIZED, "Expected specific error message for unauthorized access"