import os


class BasePage:
    def __init__(self, page):
        self._page = page

    def goto(self):
        raise RuntimeError('Subclasses must implement goto')

    def cleanup(self) -> None:
        self._page.close()

    @staticmethod
    def base_url() -> str:
        return os.getenv('BASE_URL', 'http://localhost:5063')

    def title(self):
        return self._page.title

    def navigate_home(self):
        self._page.get_by_role('link', name='Home').click()

        return self._page

    def locate_by_label(self, label):
        self._page.get_by_label(label)
