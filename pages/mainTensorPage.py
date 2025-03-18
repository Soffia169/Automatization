from elements.Link import Link
from elements.ManyWebElements import ManyWebElements
from elements.TextOutput import Textoutput
from pages.basePage import WebPage


class MainTensorPage(WebPage):
    block = Textoutput(xpath="//p[text()='Сила в людях']/parent::div")
    moreDetailsLink = Link(xpath="//p[text()='Сила в людях']/parent::div/p/a[@href='/about']")
    img_list = ManyWebElements(xpath="//h2[text()='Работаем']/parent::div/parent::div/descendant::img")

    def __init__(self, web_driver):
        url = ''
        super().__init__(web_driver, url)

    def get_url(self):
        return super()._get_url()

    def get_title(self):
        return super()._get_title()

    def wait_page_loaded(self):
        super()._wait_page_loaded()