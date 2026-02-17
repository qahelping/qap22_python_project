import allure


@allure.title("Простой тест с assertion")
def test_simple_assertion():
    """Простой тест с assertion"""
    assert 1 == 1


@allure.title("Тест сравнения строк")
def test_string_comparison():
    """Тест сравнения строк"""
    expected = "Hello World"
    actual = "Hello World!"
    assert expected == actual
