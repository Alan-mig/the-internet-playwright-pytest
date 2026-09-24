from playwright.sync_api import Page, expect


def test_home_page_headings(page: Page):
    # base_url from pytest.ini is added automatically, so "/" = home page
    page.goto("/")

    # expect() retries until the text appears or the timeout ends - no sleep needed
    expect(page.locator("h1")).to_contain_text("Welcome to the-internet")
    expect(page.locator("h2")).to_contain_text("Available Examples")