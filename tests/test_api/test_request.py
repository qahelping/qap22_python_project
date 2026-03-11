import json
import logging

import pytest
import requests

from tests.test_api.log_base import logger

DOMAIN = "http://localhost:8000"


def make_request(method, path, data=None, params=None, token=None):
    url = f"{DOMAIN}/{path}"
    payload = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    if token:
        headers['Authorization'] = f"Bearer {token}"
        logger.debug(f'{path}:: Authorization = f"Bearer {token}')
    params = params
    response = requests.request(method, url, headers=headers, data=payload, params=params)

    try:
        response.raise_for_status()
        logger.info(f'{path}:: Запрос успешен.')
        return response.json()
    except requests.exceptions.HTTPError as err:
        logging.error(f'Ошибка HTTP: {err}')
        assert False, f"Ошибка HTTP: {err}"


def get(path, params=None, token=None):
    return make_request('GET', path, data=None, params=params, token=token)

def post(path, data=None, token=None):
    return make_request('POST', path, data=data, token=token)


@pytest.mark.parametrize("email, password",
                         [("diana@example.com", "password123"), ],
                         ids=["simple user"], )
def test_login(email, password):
    payload = {"email": email, "password": password}

    response = post("auth/login", payload)

    assert response["access_token"]
    assert response["token_type"] == "bearer"


@pytest.mark.parametrize(
    "email, password",
    [
        ("diana1@example.com", "password123"),
        ("diana@example.com", "password1123"),
        ("diana1@example.com", "password1123"),
    ],
    ids=["wrong email", "wrong password", "wrong email and password"],
)
def test_login_negative(email, password):
    payload = {"email": email, "password": password}

    response = post("auth/login", payload)

    assert response["detail"] == "Incorrect email or password"


def test_healthy():
    response = make_request("GET", "health")

    assert response["status"] == "ok"
    assert response["memory"]["used_mb"]
    assert response.get("memory", False).get("percent", False)
    assert response.get("cpu", False).get("percent", False)


@pytest.mark.parametrize("email, password",
                         [("diana@example.com", "password123"), ],
                         ids=["simple user"], )
def test_get_my_task(email, password):
    payload = {"email": email, "password": password}

    response = post("auth/login", payload)


    assert response["access_token"]
    assert response["token_type"] == "bearer"

    token = response.get("access_token")

    response = get("users/me/tasks", params={'skip': 0, 'limit': 100}, token=token)

    assert len(response) == 6


