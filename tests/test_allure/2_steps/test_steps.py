import allure


@allure.step("Выполняем подготовку данных")
def prepare_data():
    return {"user_id": 123, "name": "John"}


@allure.step("Выполняем проверку {expected} == {actual}")
def check_equal(expected, actual):
    assert expected == actual


@allure.title("Тест с использованием шагов и ошибкой")
def test_with_steps():
    """Тест с использованием шагов"""
    with allure.step("Подготавливаем данные"):
        prepare_data()

    with allure.step("Проверяем ID пользователя"):
        expected = "Hello World"
        actual = "Hello World!"
        assert expected == actual, f"Expected {expected}, but got {actual}"
