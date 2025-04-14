import re
from playwright.sync_api import Page, expect


# Pytest can test utility code
def test_has_title(page: Page):
    page.goto('http://localhost:5063/')

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile('Puppy'))


def test_get_started_link(page: Page):
    page.goto('http://localhost:5063/')

    page.get_by_role('link', name='Brook').click()

    expect(page.get_by_role('heading', name='Sports')).to_be_visible()
