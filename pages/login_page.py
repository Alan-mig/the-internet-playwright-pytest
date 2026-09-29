from playwright.sync_api import Page, expect


class LoginPage:
    # Locators are defined once here - a UI change is fixed in one place
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def open(self):
        self.page.goto("/login")

    def login(self, username: str, password: str):
        # One business action instead of three low-level steps in every test
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

