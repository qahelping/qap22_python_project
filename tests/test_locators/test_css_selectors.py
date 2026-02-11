import pytest
from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab"


def get_css_element(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


@pytest.mark.selenium
def test_traditional_locators(driver):
    driver.get(URL)
    breakpoint()

    get_css_element(driver, "input")
    get_css_element(driver, ".features")
    get_css_element(driver, ".pill.pill--accent")
    get_css_element(driver, ".features .section-head")
    get_css_element(driver, "#wt-sky-root")
    get_css_element(driver, '[href="/automation-lab/subscription"]')
    get_css_element(driver, '[id="wt-sky-root"]')
    get_css_element(driver, '[class="features"]')
    get_css_element(driver, '[class="pill pill--accent"]')
    get_css_element(driver, '.case-element [data-card-id="card_39550"] .bank .bank__name')
    get_css_element(driver, "section.case-card .card--classic .balance__value")
    get_css_element(driver, ".card__holder-name + .card__bottom")
    get_css_element(driver, ".card__holder-name + .card__bottom")
    get_css_element(driver, '[href^="/automation"]')
    get_css_element(driver, '[href$="lab"]')
    get_css_element(driver, '[href$="lab"]')
    get_css_element(driver, '[href*="auto"]')
    get_css_element(driver, '[href*="auto"]')

    get_css_element(driver, ".features-grid .feature-card:first-child")
    get_css_element(driver, ".features-grid .feature-card:last-child")
    get_css_element(driver, ".features-grid .feature-card:nth-child(3)")
    get_css_element(driver, ".info-card--problem code")
