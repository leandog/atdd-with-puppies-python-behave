from features.pages.base_page import BasePage


class AdoptionPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def page_path(self):
        return '/adoption-form'
