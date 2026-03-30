from pages.login_page import LoginPage
from config.config import BASE_URL, USER_NAME, PASS_WORD
from playwright.sync_api import expect

def test_login_valid(page):

    login_page = LoginPage(page)

    login_page.load(BASE_URL)
    login_page.login(USER_NAME, PASS_WORD)

    expect(page).to_have_url("http://lct-a4g-qa.accoladeelectronics.com/device-dashboard-page")