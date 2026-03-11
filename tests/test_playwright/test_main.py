import re

import pytest
from playwright.sync_api import Page, expect


def test_homepage_has_Playwright_in_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_homepage_python(page: Page):
    page.goto("https://www.python.org/")

    # Expect a title "to contain" a substring.
    expect(page).not_to_have_title(re.compile("Welcome to Python.org"))
    expect(page).not_to_have_url(re.compile("https://www.python.org/"))


def test_homepage_python(page: Page):
    user, password = "diana@example.com", "password123"
    page.goto("http://localhost:3000/admin")

    page.locator("#id-input-login-email-input").fill(user)
    page.locator("#id-input-login-password-input").fill(password)
    page.locator('[data-qa="login-submit-button"]').click()

    page.goto("http://localhost:3000/admin")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Task Management Board"))
    expect(page.locator(".toast-container .toast-notification .toast-message")).to_be_visible()
    expect(page.locator(".toast-container.toast-message")).to_be_visible()
    expect(page.locator(".toast-container .toast-notification .toast-message")).to_contain_text("404")
    expect(page.locator(".toast-container .toast-notification .toast-message")).to_be_hidden()


@pytest.mark.only
def test_check_promocode_page(page: Page) -> None:
    page.goto("http://localhost:3000/")
    page.get_by_role("link", name="Открыть →").nth(1).click()

    expect(page.get_by_test_id("period-section")).to_be_visible()
    expect(page.get_by_test_id("period-1")).to_be_visible()
    expect(page.get_by_test_id("period-3")).to_be_visible()
    expect(page.get_by_test_id("period-12")).to_be_visible()
    expect(page.get_by_test_id("tariff-basic")).to_be_visible()
    expect(page.get_by_test_id("tariff-premium")).to_be_visible()
    expect(page.get_by_test_id("tariff-family")).to_be_visible()
    expect(page.get_by_test_id("tariff-premium")).to_be_visible()
    expect(page.get_by_test_id("tariff-family")).to_be_visible()
    expect(page.get_by_test_id("tariff-basic")).to_be_visible()

    expect(page.get_by_test_id("promo-input")).to_be_visible()
    expect(page.get_by_test_id("promo-apply-btn")).to_be_visible()

    page.get_by_test_id("promo-input").click()
    page.get_by_test_id("promo-input").fill("ALWAYS")

    page.get_by_test_id("promo-apply-btn").click()

    expect(page.get_by_test_id("promo-message")).to_be_visible()


@pytest.mark.only
@pytest.mark.browser_context_args(
    timezone_id="Europe/Berlin",
    locale="en-GB",
    viewport={
        "width": 1920,
        "height": 1080,
    },
)
def test_check_promocode_page(page: Page) -> None:
    page.goto("http://localhost:3000/")
    page.get_by_role("link1", name="Открыть →").nth(1).click()

    loc = page.locator(".tariff-card").filter(has_text="499")
    expect(loc).to_be_visible()

    text = page.locator(".tariff-card").all_text_contents()
    assert text
