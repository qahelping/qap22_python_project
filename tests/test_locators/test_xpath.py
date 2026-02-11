import pytest
from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab"


def get_xpath_element(driver, selector):
    return driver.find_element(By.XPATH, selector)


def get_element_contains_text(driver, text):
    return driver.find_element(By.XPATH, f"//*[contains(text(),'{text}')]")


@pytest.mark.selenium
def test_traditional_locators(driver):
    driver.get(URL)
    breakpoint()

    get_xpath_element(driver, "//input")
    get_xpath_element(driver, '//*[@class="header-content"]')
    get_xpath_element(driver, '//*[@class="pill pill--accent"]')

    get_xpath_element(driver, '//*[@class="brand-text"]/div[@class="brand-title"]')
    get_xpath_element(driver, '//h2[text()="Карточки подгружаются асинхронно"]')
    get_xpath_element(driver, '//h2[contains(text(),"подгружаются")]')

    get_xpath_element(driver, '//*[@aria-hidden="true"]')
    get_xpath_element(driver, '//a[contains(@href, "auto")]')
    get_xpath_element(driver, "//img[substring(@src, string-length(@src)-3)='.png']")

    get_xpath_element(driver, "//header//img")
    get_xpath_element(driver, "//div/img")
    get_xpath_element(driver, '//*[@data-card-id="card_75325"]/..')
    get_xpath_element(driver, '//*[@data-card-id="card_75325"]/..//*[@class="card card--platinum"]')
    get_xpath_element(driver, '//*[text()="6193 2772 1916 4199"]/..//*[@class="bank__tier"]')
    get_xpath_element(driver, '//*[@class="card card--platinum"][position()>3]')
    get_xpath_element(driver, '//*[@class="card card--platinum"][3]')
    get_xpath_element(driver, '//*[@class="card card--platinum"][last()]')

    get_xpath_element(
        driver, '//*[@class="card card--platinum" or @class="card card--business" or @class="card card--premium"]'
    )
    get_xpath_element(driver, '//*[@class="card card--premium" and @data-virtual="false"]')
    get_xpath_element(driver, '//*[@class="card card--premium" and @data-virtual="true"]')
    get_xpath_element(driver, '[href^="/automation"]')
    get_xpath_element(driver, '[href$="lab"]')
    get_xpath_element(driver, '[href$="lab"]')
    get_xpath_element(driver, '[href*="auto"]')
    get_xpath_element(driver, '[href*="auto"]')

    get_xpath_element(driver, ".features-grid .feature-card:first-child")
    get_xpath_element(driver, ".features-grid .feature-card:last-child")
    get_xpath_element(driver, ".features-grid .feature-card:nth-child(3)")
    get_xpath_element(driver, ".info-card--problem code")
