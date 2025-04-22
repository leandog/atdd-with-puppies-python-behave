from features.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def page_path(self):
        return '/'

    def select_puppy_by_name(self, puppy_name: str) -> None:
        self._page.get_by_role('link', name=puppy_name).click()
