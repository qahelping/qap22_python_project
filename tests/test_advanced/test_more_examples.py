import time
import urllib.request

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from files import BASE_DIR, IMG_2

url = "https://letcode.in/test"


@pytest.mark.smoke
def test_form(driver):
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    element.click()
    assert element.is_selected()


def test_select(driver):
    url = "https://the-internet.herokuapp.com/dropdown"
    driver.get(url)
    element = Select(driver.find_element(By.ID, "dropdown"))

    element.select_by_index(0)
    element.select_by_visible_text("Option 1")
    element.select_by_value("2")


def test_alert_simple(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)

    element = driver.find_element(By.CSS_SELECTOR, '[onclick="jsAlert()"]')

    element.click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert"

    alert.accept()

    element = driver.find_element(By.ID, "result")
    assert element.text == "You successfully clicked an alert"


def test_alert_confirm(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)

    element = driver.find_element(By.CSS_SELECTOR, '[onclick="jsConfirm()"]')

    element.click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm"

    alert.dismiss()

    element = driver.find_element(By.ID, "result")
    assert element.text == "You clicked: Cancel"


def test_alert_prompt(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)

    element = driver.find_element(By.CSS_SELECTOR, '[onclick="jsPrompt()"]')

    element.click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt"
    alert.send_keys("the-internet")

    alert.accept()

    element = driver.find_element(By.ID, "result")
    assert element.text == "You entered: the-internet"


def test_alert_prompt_learn_javascript(driver):
    url = "https://learn.javascript.ru/task/simple-page"
    driver.get(url)

    element = driver.find_element(By.CSS_SELECTOR, '[onclick="event.preventDefault(); runDemo(this)"]')
    element.click()
    alert = driver.switch_to.alert

    assert alert.text == "Ваше имя?"
    name = "Alena"
    alert.send_keys(name)
    alert.accept()

    assert alert.text == name

    alert.accept()


def test_navigation(driver):
    driver.get("http://the-internet.herokuapp.com/windows")
    assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"

    driver.find_element(By.CSS_SELECTOR, '[href="/windows/new"]').click()

    window_handles = driver.window_handles
    assert len(window_handles) == 2

    driver.switch_to.window(window_handles[-1])

    assert driver.current_url == "http://the-internet.herokuapp.com/windows/new"
    assert driver.title == "New Window"
    assert driver.find_element(By.TAG_NAME, "h3").text == "New Window"


def test_upload(driver):
    url = "https://letcode.in/file"
    driver.get(url)

    element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    element.send_keys(str(IMG_2))

    element = driver.find_element(By.CSS_SELECTOR, '[class="label ng-star-inserted"]')
    assert element.text == "Selected File: red_panda.png"


def test_download(driver):
    url = "https://letcode.in/file"
    driver.get(url)
    driver.find_element(By.ID, "xls").click()

    time.sleep(10)
    driver.get("chrome://downloads/")
    driver.find_element(By.ID, "main-content").is_displayed()


def test_download_experimental_option():
    file_path = "http://the-internet.herokuapp.com/download/foto2.png"
    response = urllib.request.urlopen(file_path)

    file = open(BASE_DIR / "files" / "foto2.png", "wb")
    file.write(response.read())

    file.close()


def test_upload2(driver):
    url = "http://the-internet.herokuapp.com/upload"
    driver.get(url)

    element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    element.send_keys(str(IMG_2))

    element = driver.find_element(By.ID, "file-submit")
    element.click()

    element = driver.find_element(By.TAG_NAME, "h3")
    assert element.text == "File Uploaded!"

    element = driver.find_element(By.ID, "uploaded-files")
    assert element.is_displayed()


def get_element(driver, selector, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector))
    return element


def click(driver, selector, timeout=10):
    element = get_element(driver, selector, timeout)
    element.click()


@pytest.mark.only
def test_expected_conditions(driver):
    url = "https://practice-automation.com/javascript-delays/"
    driver.get(url)

    TIME = 5

    click(driver, (By.CSS_SELECTOR, "#start"))

    picture = WebDriverWait(driver, TIME).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-image-title="rocket_liftoff"]'))
    )
    assert picture

    TIME = 15
    picture = WebDriverWait(driver, TIME).until_not(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-image-title="rocket_liftoff"]'))
    )
    assert picture is False
