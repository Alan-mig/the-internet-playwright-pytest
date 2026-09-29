from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import re

def test_login_invalid_username(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsy", "SuperSecretPassword!")
    # Assertions stay in the test, not in the page object
    expect(login_page.flash_message).to_contain_text("Your username is invalid")


def test_login_invalid_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "wrong")
    # Assertions stay in the test, not in the page object
    expect(login_page.flash_message).to_contain_text("Your password is invalid")

def test_login_valid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    # Assertions stay in the test, not in the page object
    expect(page).to_have_url(re.compile(".*/secure"))