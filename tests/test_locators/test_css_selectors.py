import pytest
from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab"


@pytest.mark.selenium
def test_traditional_locators(driver):
    driver.get(URL)
    breakpoint()

    driver.find_element(By.CSS_SELECTOR, "input")
    driver.find_element(By.CSS_SELECTOR, ".features")
    driver.find_element(By.CSS_SELECTOR, ".pill.pill--accent")
    driver.find_element(By.CSS_SELECTOR, ".features .section-head")
    driver.find_element(By.CSS_SELECTOR, "#wt-sky-root")
    driver.find_element(By.CSS_SELECTOR, '[href="/automation-lab/subscription"]')
    driver.find_element(By.CSS_SELECTOR, '[id="wt-sky-root"]')
    driver.find_element(By.CSS_SELECTOR, '[class="features"]')
    driver.find_element(By.CSS_SELECTOR, '[class="pill pill--accent"]')
    driver.find_element(By.CSS_SELECTOR, '.case-element [data-card-id="card_39550"] .bank .bank__name')
    driver.find_element(By.CSS_SELECTOR, "section.case-card .card--classic .balance__value")
    driver.find_element(By.CSS_SELECTOR, ".card__holder-name + .card__bottom")
    driver.find_element(By.CSS_SELECTOR, ".card__holder-name + .card__bottom")
    driver.find_element(By.CSS_SELECTOR, '[href^="/automation"]')
    driver.find_element(By.CSS_SELECTOR, '[href$="lab"]')
    driver.find_element(By.CSS_SELECTOR, '[href$="lab"]')
    driver.find_element(By.CSS_SELECTOR, '[href*="auto"]')
    driver.find_element(By.CSS_SELECTOR, '[href*="auto"]')

    driver.find_element(By.CSS_SELECTOR, ".features-grid .feature-card:first-child")
    driver.find_element(By.CSS_SELECTOR, ".features-grid .feature-card:last-child")
    driver.find_element(By.CSS_SELECTOR, ".features-grid .feature-card:nth-child(3)")
    driver.find_element(By.CSS_SELECTOR, ".info-card--problem code")
