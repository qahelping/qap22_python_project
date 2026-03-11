from tms_project.pages.dashboard_page import DashboardPage
from tms_project.pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("charlie@example.com", "password123")

    dashboard_page = DashboardPage(driver)
    dashboard_page.assert_that_dashboard_opened()
