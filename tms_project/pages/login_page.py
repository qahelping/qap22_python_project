from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.webdriver import WebDriver


class LoginPage:
    # LOGIN_INPUT = 'login-email-input'
    # PASSWORD_INPUT = 'login-password-input'
    # SUBMIT = 'login-submit-button'

    # LOGIN_INPUT = '#id-input-login-email-input'
    # PASSWORD_INPUT = '[id="id-input-login-password-input"]'
    # SUBMIT = '[data-qa="login-submit-button"]'

    LOGIN_INPUT = (By.ID, "id-input-login-email-input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "id-input-login-email-input")
    SUBMIT = (By.XPATH, '//*[data-qa="login-submit-button"]')

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def login(self, email, password):
        self.driver.find_element(self.LOGIN_INPUT).send_keys(email)
        self.driver.find_element(self.LOGIN_INPUT).send_keys(password)

        self.driver.find_element(self.SUBMIT).click()
