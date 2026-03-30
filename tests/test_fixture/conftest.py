import pytest


@pytest.fixture(autouse=False, scope="session")
def numbers_int():
    print('return data numbers')
    return [1, 2, 3]

@pytest.fixture(autouse=False, scope="function")
def numbers_str():
    print('return data numbers str')
    return ["1", "2", "3"]

@pytest.fixture(autouse=True, scope="session")
def numbers_int_autouse():
    print('return data numbers int autouse')
    return [1, 2, 3]
