from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab/cards"


def test_load_cards(driver):
    driver.get(URL)

    load_button = driver.find_element(By.CLASS_NAME, "trigger-btn")
    load_button.click()

    card = driver.find_elements(By.CLASS_NAME, "card")
    assert card[0].is_displayed()
