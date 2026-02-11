import pytest
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker("ru_RU")


@pytest.mark.parametrize(
    "name_str, description_str, is_public_bool",
    [
        (fake.text(max_nb_chars=15), fake.text(max_nb_chars=30), True),
        (fake.text(max_nb_chars=15), "", False),
        (fake.text(max_nb_chars=5)[0:3], "", True),
        ("< >", "", False),
    ],
)
@pytest.mark.board
@pytest.mark.usefixtures("login")
def test_create_board(driver, name_str, description_str, is_public_bool):
    submit = driver.find_element(By.CLASS_NAME, "btn-primary")
    submit.click()

    name = driver.find_elements(By.CSS_SELECTOR, '[data-qa="create-board-title-input"]')[-1]
    description = driver.find_elements(By.CLASS_NAME, "textarea-modern ")[-1]
    is_public = driver.find_elements(By.ID, "public")[-1]
    submit_create_board = driver.find_elements(By.CSS_SELECTOR, '[data-qa="create-board-submit-button"]')[-1]

    name.send_keys(name_str)
    description.send_keys(description_str)
    is_public.click() if is_public_bool else None
    submit_create_board.click()

    toast_message = driver.find_element(By.CLASS_NAME, "toast-message")
    assert toast_message.is_displayed()
