import pytest


@pytest.fixture()
def user():
    print("\n+++Вызвали фикстуру 'user'+++")
    yield {"name": "Alica"}
    print("\n+++Вернулись в фикстуру 'user'+++")


@pytest.fixture(scope="function", autouse=False)
def auto_use():
    print("\n+++Вызвали фикстуру 'auto_use'+++")
    yield {"name": "Alica"}
    print("\n+++Вернулись в фикстуру 'auto_use'+++")
