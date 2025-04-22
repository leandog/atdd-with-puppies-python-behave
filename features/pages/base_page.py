import os


class BasePage:
    @staticmethod
    def base_url() -> str:
        return os.getenv('BASE_URL', 'http://localhost:5063')

    def __init__(self, page):
        self._page = page

    def goto(self):
        self._page.goto(f'{BasePage.base_url()}{self.page_path()}')

    def locate_by_label(self, label):
        self._page.get_by_label(label)

    def navigate_home(self):
        self._page.get_by_role('link', name='Home').click()

    def page_path(self):
        raise RuntimeError('Subclasses must implement page_path')

    def title(self):
        return self._page.title
