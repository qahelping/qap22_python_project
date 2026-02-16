import pytest
from selenium.webdriver.common.by import By

URL = "http://the-internet.herokuapp.com/windows"


@pytest.mark.window
def test_windows(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, '[href="/windows/new"]').click()
    window_handles = driver.window_handles

    assert len(window_handles) == 2
    breakpoint()

    driver.switch_to.window(window_handles[-1])

    assert driver.current_url == "https://the-internet.herokuapp.com/windows/new"
    assert driver.title == "New Window"
    assert driver.find_element(By.TAG_NAME, "h3").text == "New Window"

    driver.close()
    driver.switch_to.window(window_handles[0])

    assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"
    assert driver.current_url == "https://the-internet.herokuapp.com/windows"


URL = "https://letcode.in/window"


def test_letcode_windows(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "#multi").click()
    window_handles = driver.window_handles

    breakpoint()
    assert len(window_handles) == 2

    driver.switch_to.window(window_handles[-1])

    assert "alert" in driver.current_url

    driver.switch_to.window(window_handles[0])
    driver.find_element(By.CSS_SELECTOR, "#multi").click()

    window_handles = driver.window_handles

    assert len(window_handles) == 3
    driver.switch_to.window(window_handles[-1])
    assert "dropdowns" in driver.current_url

    driver.switch_to.window(window_handles[0])
    driver.find_element(By.CSS_SELECTOR, "#multi").click()
    assert len(window_handles) == 3
