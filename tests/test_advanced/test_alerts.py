import pytest
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/javascript_alerts"


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


@pytest.mark.alert
def test_prompt_alert(driver):
    driver.get(URL)

    button = driver.find_element(By.CSS_SELECTOR, '[onclick="jsPrompt()"]')
    button.click()
    breakpoint()
    prompt = driver.switch_to.alert
    assert prompt.text == "I am a JS prompt"

    text = "TRY TO USE ALETS"
    prompt.send_keys(text)
    prompt.accept()

    result = driver.find_element(By.CSS_SELECTOR, "#result")
    assert text in result.text
