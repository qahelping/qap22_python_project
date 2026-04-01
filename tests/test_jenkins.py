import pytest
import requests


def test_sum():
    assert 2 + 2 == 4


def test_upper():
    assert "jenkins".upper() == "JENKINS"


def test_in_list():
    users = ["admin", "qa", "dev"]
    assert "qa" in users


def test_dict_value():
    data = {"status": "ok", "code": 200}
    assert data["code"] == 200


def test_bool():
    is_running = True
    assert is_running is True


def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


code = 200


def get_status(code):
    if code == 200:
        return "success"
    return "error"


def test_failed_example():
    assert 10 == 5


# список всех породы
def test_get_all_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "akita" in data["message"]


# рандомное изображение собак
def test_get_random_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https://")


# одно рандомные изображения по породе
@pytest.mark.parametrize("breed", ["spaniel", "retriever", "pug"])
def test_random_image_by_breed(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "https://" in data["message"]


#  изображения sub-breed
@pytest.mark.parametrize("breed, sub_breed", [
    ("bulldog", "english"),
    ("bulldog", "boston"),
    ("bulldog", "french"),
])
def test_images_by_sub_breed(breed, sub_breed):
    url = (f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images")
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)


# рандомное изображение под-породы afghan
def test_random_image_from_sub_breed():
    url = "https://dog.ceo/api/breed/hound/afghan/images/random"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "success"
