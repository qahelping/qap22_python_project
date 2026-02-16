import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://practice-automation.com/javascript-delays/"

TIME = 5


def wait_for_clickable(driver, selector):
    return WebDriverWait(driver, TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))


def get_element(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return WebDriverWait(driver, TIME).until(EC.visibility_of(element))


def element_is_located(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return WebDriverWait(driver, TIME).until(EC.presence_of_element_located(element))


def wait_until_not_element_located(driver, selector, TIME):
    return WebDriverWait(driver, TIME).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))


@pytest.mark.ec
def test_ec(driver):
    driver.get(URL)

    element = wait_for_clickable(driver, "#start")
    element.click()

    element_rocket = get_element(driver, '[data-image-title="rocket_liftoff"]')
    assert element_rocket

    img = wait_until_not_element_located(driver, '[data-image-title="rocket_liftoff"]', 15)

    assert img is False
