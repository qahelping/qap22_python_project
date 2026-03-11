import json
import shlex
from typing import Union

import pytest
import requests


def make_curl_from_request(
    request: Union[requests.Request, requests.PreparedRequest],
    compressed: bool = False,
    verbose: bool = False
) -> str:
    """
    Преобразует объект запроса requests в команду curl.

    Args:
        request: Объект Request или PreparedRequest из библиотеки requests
        compressed: Добавить флаг --compressed для сжатых ответов
        verbose: Добавить флаг -v для подробного вывода

    Returns:
        str: Команда curl для выполнения в терминале
    """
    # Подготавливаем запрос, если это не PreparedRequest
    if isinstance(request, requests.Request):
        prepared = request.prepare()
    elif isinstance(request, requests.PreparedRequest):
        prepared = request
    else:
        raise TypeError("Request must be requests.Request or requests.PreparedRequest")

    # Начинаем сборку команды
    curl_parts = ["curl"]

    # Добавляем флаги
    if verbose:
        curl_parts.append("-v")

    if compressed:
        curl_parts.append("--compressed")

    # Добавляем метод (если не GET)
    method = prepared.method
    if method and method.upper() != "GET":
        curl_parts.append(f"-X {method}")

    # Добавляем заголовки
    headers = prepared.headers
    for key, value in headers.items():
        # Экранируем значение для безопасного использования в командной строке
        escaped_value = shlex.quote(str(value))
        curl_parts.append(f"-H {key}: {escaped_value}")

    # Добавляем тело запроса
    if prepared.body:
        # Проверяем, не является ли тело запроса данными формы
        content_type = headers.get('Content-Type', '')
        if 'application/x-www-form-urlencoded' in content_type:
            # Для form data используем --data
            curl_parts.append(f"--data {shlex.quote(prepared.body)}")
        else:
            # Для остальных случаев используем --data-binary
            curl_parts.append(f"--data-binary {shlex.quote(prepared.body)}")

    # Добавляем URL
    curl_parts.append(shlex.quote(prepared.url))

    return " ".join(curl_parts)


def make_curl_from_response(response: requests.Response, **kwargs) -> str:
    """
    Преобразует объект ответа requests в команду curl для повторения запроса.

    Args:
        response: Объект Response из библиотеки requests
        **kwargs: Дополнительные аргументы для make_curl_from_request

    Returns:
        str: Команда curl для выполнения в терминале
    """
    return make_curl_from_request(response.request, **kwargs)


@pytest.mark.parametrize(
    "email, password",
    [
        ("diana@example.com", "password123"),
        ("admin@example.com", "admin123"),
    ],
    ids=["simple user", "admin"],
)
def test_login(email, password):
    url = "http://localhost:8000/auth/login"

    payload = json.dumps({"email": email, "password": password})

    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    сookies = response.cookies
    print(сookies)
    res_json = response.json()

    assert response.status_code == 200
    assert res_json["access_token"]
    assert res_json["token_type"] == "bearer"


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
    url = "http://localhost:3000/auth/login"

    payload = json.dumps({"email": email, "password": password})

    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    curl_from_response = make_curl_from_response(response)
    print("\nИз ответа:")
    print(curl_from_response)

    res_json = response.json()

    # assert res_json['access_token']
    # assert res_json['token_type'] == 'bearer'

    assert response.status_code == 401
    assert res_json["detail"] == "Incorrect email or password"

# url = "http://localhost:8000/boards/"
#
# payload = json.dumps({
#   "title": "23e4r5t",
#   "description": "At quisquam distinctio magnam consequatur odit facilis animi reprehenderit. Voluptatem architecto doloremque in recusandae nostrum rerum atque minima. Similique ipsum vitae magnam ut nobis. Ipsa soluta minus repellendus repellat id quas vel velit suscipit. A alias commodi omnis sed dolor ipsam beatae.",
#   "public": False
# })
# headers = {
#   'Authorization': f'Bearer {res_json["access_token"]}',
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
