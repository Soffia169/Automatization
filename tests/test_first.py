import allure

from pages.mainSbisPage import MainSbisPage
from pages.mainTensorPage import MainTensorPage
from tests.baseTest import BaseSeleniumTest


class FirstTest(BaseSeleniumTest):
    @allure.title("Переход со страницы Sbis")
    @allure.description("Проверка перехода (со страницы Sbis) и содержимого страницы на сайте Tensor")
    def test(self):
        expected_url_tensor = "https://tensor.ru/"
        page = MainSbisPage(self.driver)
        with allure.step("Нажимаем на кнопку 'Контакты'"):
            page.contactButton.click()
        with allure.step("Нажимаем на ссылку с остальными офисами"):
            page.otherOfficeLink.click()
            self.take_screenshot()
        with allure.step("Нажимаем на логотип 'Tensor'"):
            page.tensorLink.click()
        main_window = self.driver.current_window_handle
        self.switch_on_new_tab(main_window)

        page2 = MainTensorPage(self.driver)
        with allure.step(f"Проверяем, что выполнен переход на URL {expected_url_tensor}"):
            assert expected_url_tensor in page2.getURL()
            self.take_screenshot()


