import requests
import allure
from data import BASE_URL
from response_messages import ERROR_NO_INGREDIENTS, ERROR_INVALID_INGREDIENT

class TestCreateOrder:
    # с авторизацией
    @allure.title("Create order with authorization")
    def test_create_order_with_auth(self, registered_user):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        response = requests.post(f'{BASE_URL}/orders', json=payload, headers=registered_user["headers"])
        assert response.status_code == 200, "Expected status code 200 for successful order creation"
        assert response.json()["success"] is True, "Expected 'success' to be True in response"

    # без авторизации
    @allure.title("Create order without authorization")
    def test_create_order_without_auth(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        response = requests.post(f'{BASE_URL}/orders', json=payload)
        assert response.status_code == 200, "Expected status code 200 for unauthorized order creation"
        assert response.json()["success"] is True, "Expected 'success' to be True in response"

    # ? с ингредиентами
    # непонимаю, что значит "с ингредиентами" в контексте теста создания заказа, так как в предыдущих тестах уже используются ингредиенты.

    # без ингредиентов
    @allure.title("Create order without ingredients")
    def test_create_order_without_ingredients(self):
        payload = {
            "ingredients": []
        }
        response = requests.post(f'{BASE_URL}/orders', json=payload)
        assert response.status_code == 400, "Expected status code 400 for order creation without ingredients"
        assert response.json()["success"] is False, "Expected 'success' to be False in response"
        assert ERROR_NO_INGREDIENTS in response.text, "Expected error message for empty ingredients"

    # с неверным хешем ингредиентов
    @allure.title("Create order with invalid ingredient hash")
    def test_create_order_with_invalid_ingredient_hash(self):
        payload = {
            "ingredients": ["invalid_hash"]
        }
        response = requests.post(f'{BASE_URL}/orders', json=payload)
        assert response.status_code == 400, "Expected status code 400 for order creation with invalid ingredient hash"
        assert response.json()["success"] is False, "Expected 'success' to be False in response"
        assert ERROR_INVALID_INGREDIENT in response.text, "Expected error message for invalid ingredient hash"