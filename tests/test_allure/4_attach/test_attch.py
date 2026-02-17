import json

import allure
import pytest

from tests.test_allure.allure_attach import CommonFormatter


@pytest.fixture
def common():
    """Fixture for save and transactions test values between steps, for example data class for module."""

    class Common:
        def __getattr__(self, item):
            return self.__dict__.get(item)

        def to_html(self):
            """Convert Common object to HTML representation."""
            return CommonFormatter.to_html(self.__dict__)

    return Common()


def test_with_json_attachment():
    """Тест с JSON вложением"""
    data = {"user": "john", "status": "active", "id": 123}

    with allure.step("Создаем JSON данные"):
        json_data = json.dumps(data, indent=2)

    with allure.step("Добавляем JSON вложение"):
        allure.attach(json_data, "user_data.json", allure.attachment_type.JSON)

    assert data["status"] == "active"


def test_with_text_attachment():
    """Тест с текстовым вложением"""
    log_content = """
    INFO: Starting test
    DEBUG: User logged in
    WARNING: Low memory
    ERROR: Database connection failed
    """

    allure.attach(log_content, "test_log.txt", allure.attachment_type.TEXT)
    assert True


def test_with_image_attachment():
    """Тест с изображением"""
    image_data = "Png image data (simulated)"
    allure.attach(image_data, "files/avatar1.jpeg", allure.attachment_type.PNG)
    assert True


def test_common_fixture_with_html_attachment(common):
    """Тест с использованием фикстуры common и выводом красивого HTML в Allure отчет"""

    with allure.step("Инициализация данных в common фикстуре"):
        # Добавляем различные типы данных в common
        common.user_id = 12345
        common.username = "test_user"
        common.email = "test_user@example.com"
        common.is_active = True
        common.roles = ["admin", "user", "moderator"]
        common.balance = 1250.50
        common.metadata = {"created_at": "2026-02-17", "last_login": "2026-02-17 10:30:00"}
        common.status = "active"
        common.permissions = ["read", "write", "delete"]

    with allure.step("Выполнение проверок"):
        assert common.user_id == 12345
        assert common.username == "test_user"
        assert common.is_active is True
        assert len(common.roles) == 3

    with allure.step("Генерация HTML из common фикстуры"):
        html_content = common.to_html()

    with allure.step("Прикрепление HTML в Allure отчет"):
        allure.attach(html_content, name="Common Fixture Data", attachment_type=allure.attachment_type.HTML)

    # Финальная проверка
    assert common.balance > 0
