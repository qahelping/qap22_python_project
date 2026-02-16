import os
import time

import pytest
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/download"


@pytest.mark.download
def test_download(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, "//a[2]").click()

    time.sleep(2)

    driver.get("chrome://downloads/")
    breakpoint()
    assert driver.find_element(By.ID, "main-content").is_displayed()
    assert driver.find_element(By.ID, "file-link").text == "file.json"


URL = "https://the-internet.herokuapp.com/upload"


@pytest.mark.upload
def test_upload(driver):
    driver.get(URL)
    driver.find_element(By.ID, "file-upload").send_keys(os.path.abspath("../qap22_python_project/files/file.json"))

    time.sleep(2)

    driver.find_element(By.ID, "file-submit").submit()
    breakpoint()
    assert driver.find_element(By.ID, "uploaded-files").is_displayed()
