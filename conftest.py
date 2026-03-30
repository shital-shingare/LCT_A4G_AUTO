import pytest
from playwright.sync_api import sync_playwright
from config.config import BASE_URL, DASHBOARD_URL, BROWSER, HEADLESS
from pages.dashboard_page import Dashboard

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser_type = getattr(playwright_instance, BROWSER)
    browser = browser_type.launch(headless=HEADLESS)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def dashboard_page(page):
    dashboard = Dashboard(page)
    dashboard.go_to_dashboard(DASHBOARD_URL)
    return dashboard