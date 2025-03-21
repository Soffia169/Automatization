from selenium.webdriver import ActionChains

from elements.baseElement import WebElement


class Link(WebElement):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def click(self):
        super()._click()

    def get_text(self):
        return super()._get_text()