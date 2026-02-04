# import pytest
#
import pytest


@pytest.mark.usefixtures("user")
def test_user(user):
    print("\n+++Запустили тест 'test_user'+++")
    assert user.get("name") == "Alica"
