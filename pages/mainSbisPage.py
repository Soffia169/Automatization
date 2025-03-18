from elements.Button import Button
from elements.Link import Link
from elements.ListElements import ListWebElements
from elements.TextOutput import Textoutput
from pages.basePage import WebPage


class MainSbisPage(WebPage):
    contactButton = Button(xpath="//div[@class='sbisru-Header']/descendant::div[contains(text(), 'Контакты')]")
    otherOfficeLink = Link(xpath="//a[@href ='/contacts']/span")
    tensorLink = Link(xpath="//div[@id = 'contacts_clients']/descendant::a[@href='https://tensor.ru/']")
    region_link = Link(xpath="//h1[text()='Контакты']/parent::div/following-sibling::div/span/span")
    list_partners = ListWebElements(xpath="//div[contains(@class, 'sbisru-Contacts-List__name')]")
    region_41_link = Link(xpath="//span[text()='41 Камчатский край']")
    city_title = Textoutput(xpath="//div[@id='city-id-2']")
    download_versions_link = Link(xpath="//ul[contains(@class, 'sbisru-Footer__list')]/descendant::a[@href='/download']")
    download_link = Link(xpath="//a[@href ='https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
    plugin_button = Button(xpath="//div[contains(@class, 'controls-Checked__checked') and @data-id='plugin']")
    os_button = Button(xpath="//div[contains(@class, 'controls-Checked__checked') and @id='ws-eu0efp824891742273019665']")

    def __init__(self, web_driver):
        url = 'https://sbis.ru'
        super().__init__(web_driver, url)

    def get_url(self):
        return super()._get_url()

    def get_title(self):
        return super()._get_title()

    def wait_page_loaded(self):
        super()._wait_page_loaded()