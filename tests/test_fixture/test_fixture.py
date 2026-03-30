import pytest

def test_numbers1(numbers_int_autouse):
    assert numbers_int_autouse == [1, 2, 3]

def test_numbers2(numbers_int):
    assert numbers_int == [1, 2, 3]

lst = [0]

@pytest.fixture(scope="session")
def data_session():
    print("\nСоздали session data")
    return lst


@pytest.fixture(scope="function")
def data():
    print("\nСоздали data")
    return []


def test_one(data_session):
    data_session.append(1)
    assert data_session == [0, 1]


def test_two(data_session):
    data_session.append(2)
    assert data_session == [0, 1, 2]
