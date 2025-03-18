import allure

import os

from pages.mainSbisPage import MainSbisPage
from pages.mainTensorPage import MainTensorPage
from tests.baseTest import BaseSeleniumTest


class TensorTest(BaseSeleniumTest):
    @allure.title("Первый сценарий")
    @allure.description("Проверка перехода (со страницы Sbis) и содержимого страницы на сайте Tensor")
    def test_1(self):
        expected_url_tensor = "https://tensor.ru/"
        expected_text_block = "Сила в людях"
        expected_url_about = "https://tensor.ru/about"

        with allure.step("Переходим на главную страницу сайта 'Saby'"):
            page = MainSbisPage(self.driver)
            self.take_screenshot()
        with allure.step("Нажимаем на кнопку 'Контакты'"):
            page.contactButton.click()
        with allure.step("Нажимаем на ссылку с остальными офисами"):
            page.otherOfficeLink.click()
            self.take_screenshot()
        with allure.step("Нажимаем на логотип 'Tensor'"):
            page.tensorLink.click()
        with allure.step("Переключаемся на открывшуюся вкладку"):
            main_window = self.driver.current_window_handle
            self.switch_on_new_tab(main_window)
        with allure.step(f"Проверяем, что выполнен переход на URL {expected_url_tensor}"):
            page2 = MainTensorPage(self.driver)
            self.assertEqual(expected_url_tensor, page2.get_url())
            self.take_screenshot()
        with allure.step(f"Проверяем, что есть блок с текстом {expected_text_block}"):
            page2.block.scroll_to_element()
            self.assertIn(expected_text_block, page2.block.get_text())
        with allure.step("Нажимаем на ссылку 'Подробнее' в блоке"):
            page2.moreDetailsLink.click()
        with allure.step(f"Проверяем, что выполнен переход на URL {expected_url_about}"):
            self.assertEqual(page2.get_url(), expected_url_about)
            self.take_screenshot()
        with allure.step("Проверяем, что все фотографии из раздела 'Работаем' одинаковой ширины и высоты"):
            widthImg = page2.img_list[0].get_attribute("width")
            heightImg = page2.img_list[0].get_attribute("height")
            for img in page2.img_list:
                self.assertEqual(img.get_attribute("width"), widthImg)
                self.assertEqual(img.get_attribute("height"), heightImg)

    @allure.title("Второй сценарий")
    @allure.description("Проверка перехода (со страницы Sbis) и отображения информации разных регионов")
    def test_2(self):
        expected_region = "Свердловская обл."
        expected_region_41 = "Камчатский край"
        expected_region_41_url = "41-kamchatskij-kraj"
        expected_region_41_title = "Saby Контакты — Камчатский край"

        with allure.step("Переходим на главную страницу сайта 'Saby'"):
            page = MainSbisPage(self.driver)
            self.take_screenshot()
        with allure.step("Нажимаем на кнопку 'Контакты'"):
            page.contactButton.click()
        with allure.step("Нажимаем на ссылку с остальными офисами"):
            page.otherOfficeLink.click()
            self.take_screenshot()
        with allure.step("Проверяем, что определился наш регион"):
            self.assertEqual(page.region_link.get_text(), expected_region)
        with allure.step("Проверяем, что есть список партнёров"):
            title_partner_list = page.list_partners.get_text()
            for title_partner in title_partner_list:
                with allure.step(f"Имя партнёра: {title_partner}"):
                    self.assertIsNotNone(title_partner)
        with allure.step("Изменяем регион на Камчатский край"):
            page.region_link.click()
            page.region_41_link.click()
        with allure.step("Проверяем, что подставился выбранный регион"):
            page.wait_page_loaded()
            self.assertEqual(page.region_link.get_text(), expected_region_41)
        with allure.step("Проверяем, что выбранный регион отобразился в URL и в названии вкладки"):
            self.assertIn(expected_region_41_url, page.get_url())
            self.assertEqual(page.get_title(), expected_region_41_title)
        with allure.step("Проверяем, что список партнёров изменился"):
            title_partner_list_2 = page.list_partners.get_text()
            self.assertNotEqual(title_partner_list, title_partner_list_2)
            self.take_screenshot()

    @allure.title("Третий сценарий")
    @allure.description("Проверка корректного скачивания файла")
    def test_3(self):
        download_path = os.path.join(os.path.dirname(__file__), "downloads")

        with allure.step("Переходим на главную страницу сайта 'Saby'"):
            page = MainSbisPage(self.driver)
            self.take_screenshot()
        with allure.step("Переходим по ссылке 'Скачать локальные версии'"):
            page.download_versions_link.click()
        with allure.step("Проверяем, что выбрана вкладка 'Saby Plugin'"):
            self.assertIsNotNone(page.plugin_button)
        with allure.step("Проверяем, что выбрана ОС 'Windows'"):
            self.assertIsNotNone(page.os_button)
            self.take_screenshot()
        with allure.step("Нажимаем на ссылку для загрузки"):
            page.download_link.click()
        with allure.step("Проверяем, что файл скачался и имеет корректное расширение"):
            downloaded_file = self.wait_for_download(download_path)
            full_path = os.path.join(download_path, downloaded_file)
            assert os.path.exists(full_path), "Файл не был скачан"
            assert downloaded_file.endswith('.exe'), "Некорректное расширение файла"
        with allure.step("Проверяем, что размер скачанного файла совпадает с указаным на сайте"):
            expected_size_mb = float(page.download_link.get_text().split()[2])
            file_size_bytes = os.path.getsize(full_path)
            file_size_mb = round(file_size_bytes / (1024 * 1024), 2)
            self.assertEqual(file_size_mb, expected_size_mb)