from elements.Button import Button
from elements.Link import Link
from elements.baseElement import WebElement
from pages.basePage import WebPage


class MainSbisPage(WebPage):
    def __init__(self, web_driver):
        url = 'https://sbis.ru'
        super().__init__(web_driver, url)

    contactButton = Button(xpath="//div[@class='sbisru-Header']/descendant::div[contains(text(), 'Контакты')]")
    otherOfficeLink = Link(xpath="//a[@href ='/contacts']/span")
    tensorLink = Link(xpath="//div[@id = 'contacts_clients']/descendant::a[@href='https://tensor.ru/']")