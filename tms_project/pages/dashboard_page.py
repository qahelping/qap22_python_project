from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class DashboardPage:
    CREATE_BOARD_BUTTON = (By.CSS_SELECTOR, '[data-qa="dashboard-create-board-button"]')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.url = "/dashboard"
        self.title = "Task Management Board"

    def assert_that_dashboard_opened(self):
        assert self.url in self.driver.current_url
        assert self.title == self.driver.title
        assert self.driver.find_element(self.CREATE_BOARD_BUTTON).is_displayed()
