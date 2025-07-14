import random
import requests
from data import BASE_URL

def create_test_user():
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

    return {
        "email": email,
        "password": password,
        "accessToken": token,
        "headers": {"Authorization": token}
    }

def delete_test_user(headers):
    response = requests.delete(f"{BASE_URL}/auth/user", headers=headers)
    assert response.status_code == 202, f"Failed to delete user: {response.status_code} {response.text}"
