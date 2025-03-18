from selenium.webdriver import ActionChains

from elements.baseElement import WebElement


class Textoutput(WebElement):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_text(self):
        return super()._get_text()

    def scroll_to_element(self):
        super()._scroll_to_element()