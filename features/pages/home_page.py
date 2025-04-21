import os
import re
from playwright.sync_api import expect

class HomePage:
    def __init__(self, browser):
        self.page = browser.new_page()

    def goto(self):
        self.page.goto(f'{HomePage.base_url()}/')

        return self.page

    def select_puppy_by_name(self, puppy_name: str) -> None:
        self.page.get_by_role('link', name=puppy_name).click()

    def cleanup(self) -> None:
        self.page.close()

    @staticmethod
    def base_url() -> str:
        return os.getenv('BASE_URL', 'http://localhost:5063')

    def title(self):
        return self.page.title

    def navigate_home(self):
        self.page.get_by_role('link', name='Home').click()

        return self.page


