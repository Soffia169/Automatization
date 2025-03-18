from elements.baseElement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class ManyWebElements(WebElement):

    def __getitem__(self, item):
        elements = self._find()
        return elements[item]

    def _find(self, timeout=10):
        elements = []

        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_all_elements_located(self._locator)
            )
        except:
            print('Elements not found on the page!', 'red')

        return elements

    def _get_text(self):
        elements = self._find()
        result = []

        for element in elements:
            text = ''

            try:
                text = str(element.text)
            except Exception as e:
                print('Error: {0}'.format(e))

            result.append(text)

        return result

    def _get_attribute(self, attr_name):
        results = []
        elements = self._find()

        for element in elements:
            results.append(element.get_attribute(attr_name))

        return results