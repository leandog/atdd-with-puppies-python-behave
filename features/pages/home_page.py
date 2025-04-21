from features.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, browser.new_page())

    def goto(self):
        self.page.goto(f'{HomePage.base_url()}/')

        return self.page

    def select_puppy_by_name(self, puppy_name: str) -> None:
        self.page.get_by_role('link', name=puppy_name).click()
