import requests
import allure
from data import BASE_URL

class TestRetrieveOrderInfo:
    # Получение заказов конкретного пользователя
    # авторизованный пользователь
    @allure.title("Retrieve user orders with authorization")
    def test_retrieve_user_orders_with_auth(self, user_with_order):
        response = requests.get(f'{BASE_URL}/orders', headers=user_with_order)
        assert response.status_code == 200, "Expected status code 200 for successful order retrieval"
        assert response.json()["success"] is True, "Expected 'success' to be True in response"
        assert len(response.json()["orders"]) > 0, "Expected at least one order in the response"

    # неавторизованный пользователь
    @allure.title("Retrieve user orders without authorization")
    def test_retrieve_user_orders_without_auth(self):
        response = requests.get(f'{BASE_URL}/orders')
        assert response.status_code == 401, "Expected status code 401 for unauthorized order retrieval"
        assert response.json()["success"] is False, "Expected 'success' to be False in response"
        assert response.json()["message"] == "You should be authorised", "Expected specific error message for unauthorized access"