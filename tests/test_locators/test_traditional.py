import pytest
from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab"


@pytest.mark.selenium
def test_traditional_locators(driver):
    driver.get(URL)
    breakpoint()
    driver.find_element(By.ID, "card-number-input").is_displayed()
    driver.find_element(By.CLASS_NAME, "card-input").is_displayed()
    driver.find_element(By.LINK_TEXT, "Назад").is_displayed()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Назад").is_displayed()
    driver.find_element(By.NAME, "description").is_displayed()
    driver.find_element(By.TAG_NAME, "section").is_displayed()
    driver.find_elements(By.CLASS_NAME, "feature-link")[0].is_displayed()
