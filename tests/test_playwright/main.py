from playwright.sync_api import sync_playwright


def run(playwright):
    firefox = playwright.webkit
    browser = firefox.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
