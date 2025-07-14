import pytest
import requests
from data import BASE_URL, VALID_INGREDIENTS
from helpers import create_test_user, delete_test_user

@pytest.fixture
def user_with_order(registered_user):
    # Create an order for the registered user
    requests.post(f"{BASE_URL}/orders", json={"ingredients": VALID_INGREDIENTS}, headers=registered_user["headers"])
    
    return registered_user["headers"]

@pytest.fixture
def registered_user():
    user = create_test_user()
    yield user
    delete_test_user(user["headers"])