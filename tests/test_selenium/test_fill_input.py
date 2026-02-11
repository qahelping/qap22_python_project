import pytest
from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab/subscription"


def test_fill_promocode_invalid(driver):
    driver.get(URL)

    promo_input = driver.find_element(By.CSS_SELECTOR, ".promo-input-wrapper input")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promo_input)

    promo_input.send_keys("12345")

    promo_apply_btn = driver.find_element(By.CLASS_NAME, "promo-apply-btn")
    assert promo_apply_btn.is_enabled() is False
    assert promo_apply_btn.get_attribute("disabled") is not None

    promo_apply_btn.click()

    promo_message_error = driver.find_element(By.CSS_SELECTOR, ".promo-message.error")
    assert promo_message_error.text == "Промокод не найден"
    assert promo_message_error.value_of_css_property("color") == "rgba(255, 90, 95, 0.95)"


@pytest.mark.only
def test_fill_promocode_valid(driver):
    driver.get(URL)

    promo_input = driver.find_element(By.CSS_SELECTOR, ".promo-input-wrapper input")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promo_input)

    promo_input.send_keys("12345")

    promo_apply_btn = driver.find_element(By.CLASS_NAME, "promo-apply-btn")
    assert promo_apply_btn.is_enabled()
    assert promo_apply_btn.get_attribute("disabled") is None

    promo_apply_btn.click()

    promo_message_error = driver.find_element(By.CSS_SELECTOR, ".promo-message.error")
    assert promo_message_error.text == "Промокод применен"
