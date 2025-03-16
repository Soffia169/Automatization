from elements.baseElement import WebElement
from pages.basePage import WebPage


class MainTensorPage(WebPage):
    def __init__(self, web_driver):
        url = ''
        super().__init__(web_driver, url)

    # contactButton = WebElement(xpath="//div[@class='sbisru-Header']/descendant::div[contains(text(), 'Контакты')]")
    # otherOfficeLink = WebElement(xpath="//a[@href ='/contacts']/span")
    # tensorLink = WebElement(xpath="//div[@id = 'contacts_clients']/descendant::a[@href='https://tensor.ru/']")