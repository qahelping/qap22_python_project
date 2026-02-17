import allure
import pytest


@allure.epic("Test epic")
@allure.feature("Test feature")
class TestEx:
    @allure.story("Test story")
    class TestCl1:

        @allure.tag("smoke")
        @allure.severity(allure.severity_level.BLOCKER)
        def test_blocker_issue(self):
            """Критический баг"""
            assert True

        @allure.tag("regression")
        @allure.severity(allure.severity_level.NORMAL)
        def test_regression_case(self):
            """Регрессионный тест"""
            assert 1 + 1 == 2

        @allure.tag("functional")
        @allure.severity(allure.severity_level.MINOR)
        def test_functional_case(self):
            """Функциональный тест"""
            result = len("Hello World")
            assert result == 11

        def test_functional_case_1(self, prepare):
            """Функциональный тест"""
            allure.severity(allure.severity_level.MINOR)


@pytest.fixture()
def prepare(): ...
