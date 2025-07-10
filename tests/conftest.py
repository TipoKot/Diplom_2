import pytest
import requests
import random
from data import BASE_URL

@pytest.fixture
def registered_user():
    email = f"user{random.randint(1000, 9999)}@example_07.com"
    password = "password123"
    name = "Test User"
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=payload)
    assert response.status_code == 200
    token = response.json().get("accessToken")
    assert token is not None

    user_data = {
        "email": email,
        "password": password,
        "accessToken": token,
        "headers": {"Authorization": token}
    }

    yield user_data

    delete_response = requests.delete(f"{BASE_URL}/auth/user", headers=user_data["headers"])
    assert delete_response.status_code == 202, f"Failed to delete user: {delete_response.status_code} {delete_response.text}"

@pytest.fixture
def user_with_order(registered_user):
    # Create an order for the registered user
    order_payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    response = requests.post(f"{BASE_URL}/orders", json=order_payload, headers=registered_user["headers"])
    assert response.status_code == 200, f"Failed to create order: {response.status_code} {response.text}"
    
    return registered_user["headers"]
