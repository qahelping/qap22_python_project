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
