from features.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self._page.goto(f'{HomePage.base_url()}/')

    def select_puppy_by_name(self, puppy_name: str) -> None:
        self._page.get_by_role('link', name=puppy_name).click()
