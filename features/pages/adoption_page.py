from features.pages.base_page import BasePage


class AdoptionPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, browser.new_page())

    def goto(self):
        self.page.goto(f'{BasePage.base_url()}/adoption-form')

        return self.page
