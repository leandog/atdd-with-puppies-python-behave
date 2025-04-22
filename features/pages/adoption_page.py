from features.pages.base_page import BasePage


class AdoptionPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self._page.goto(f'{BasePage.base_url()}/adoption-form')
