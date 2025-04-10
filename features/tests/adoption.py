import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://cnn.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("CNN"))

def test_get_started_link(page: Page):
    page.goto("https://cnn.com/")

    page.get_by_role("link", name="Sports").click()

    expect(page.get_by_role("heading", name="Sports")).to_be_visible()
