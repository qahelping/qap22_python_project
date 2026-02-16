import pytest
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/iframe"


@pytest.mark.frame
def test_frame(driver):
    driver.get(URL)

    driver.switch_to.frame(driver.find_element(By.ID, "mce_0_ifr"))
    text = driver.find_element(By.CSS_SELECTOR, "#tinymce p")
    assert text.text == "Your content goes here."

    driver.switch_to.default_content()
