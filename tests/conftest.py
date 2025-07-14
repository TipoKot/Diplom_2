import pytest
import requests
from data import BASE_URL
from helpers import create_test_user, delete_test_user

@pytest.fixture
def user_with_order(registered_user):
    # Create an order for the registered user
    order_payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    response = requests.post(f"{BASE_URL}/orders", json=order_payload, headers=registered_user["headers"])
    assert response.status_code == 200, f"Failed to create order: {response.status_code} {response.text}"
    
    return registered_user["headers"]

@pytest.fixture
def registered_user():
    user = create_test_user()
    yield user
    delete_test_user(user["headers"])