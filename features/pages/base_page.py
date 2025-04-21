import os


class BasePage:
    def __init__(self, browser, page):
        self.page = browser.new_page()

    def goto(self):
        raise RuntimeError('Subclasses must implement goto')

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
