from selenium.webdriver import ActionChains

from elements.baseElement import WebElement


class Link(WebElement):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()