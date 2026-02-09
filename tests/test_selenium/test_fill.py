import pytest
from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab/subscription"


@pytest.mark.only
def test_fill_promocode_invalid(driver):
    driver.get(URL)

    promo_input = driver.find_element(By.CSS_SELECTOR, ".promo-input-wrapper input")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promo_input)

    promo_input.send_keys("12345")

    promo_apply_btn = driver.find_element(By.CLASS_NAME, "promo-apply-btn")
    assert promo_apply_btn.is_enabled()

    promo_apply_btn.click()

    promo_message_error = driver.find_element(By.CSS_SELECTOR, ".promo-message.error")
    assert promo_message_error.text == "Промокод не найден"


@pytest.mark.only
def test_fill_promocode_valid(driver):
    driver.get(URL)

    promo_input = driver.find_element(By.CSS_SELECTOR, ".promo-input-wrapper input")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promo_input)

    promo_input.send_keys("12345")

    promo_apply_btn = driver.find_element(By.CLASS_NAME, "promo-apply-btn")
    assert promo_apply_btn.is_enabled()

    promo_apply_btn.click()

    promo_message_error = driver.find_element(By.CSS_SELECTOR, ".promo-message.error")
    assert promo_message_error.text == "Промокод применен"
