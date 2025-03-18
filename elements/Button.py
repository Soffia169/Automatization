from selenium.webdriver import ActionChains

from elements.baseElement import WebElement


class Button(WebElement):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def click(self):
        super()._click()