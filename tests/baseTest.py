import unittest

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import uuid


class BaseSeleniumTest(unittest.TestCase):
    """Базовый класс для Selenium тестов"""

    @classmethod
    def setUpClass(cls):
        # cls.base_url = os.getenv('BASE_URL', 'https://example.com')
        # cls.browser = os.getenv('BROWSER', 'chrome').lower()
        # cls.headless = os.getenv('HEADLESS', 'false').lower() == 'true'
        cls.base_url = "https://sbis.ru"
        cls.browser = 'chrome'
        cls.headless = False

    def setUp(self):
        self._init_driver()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def _init_driver(self):
        """Инициализация WebDriver с выбранными опциями"""
        if self.browser == 'chrome':
            from selenium.webdriver.chrome.options import Options
            options = Options()
            if self.headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Chrome(options=options)

        elif self.browser == 'firefox':
            from selenium.webdriver.firefox.options import Options
            options = Options()
            if self.headless:
                options.add_argument("-headless")
            self.driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f'Unsupported browser: {self.browser}')

    def tearDown(self):
        if self._test_has_failed():
            self.take_screenshot()
        self.driver.quit()

    def _test_has_failed(self):
        return any(error for (method, error) in self._outcome.errors)

    def take_screenshot(self):
        """Сделать скриншот"""
        screenshot_name = f'{self._testMethodName}_{str(uuid.uuid4())}'
        png_bytes = self.driver.get_screenshot_as_png()
        allure.attach(
            png_bytes,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )

    def open_path(self, path='/'):
        """Открыть указанный путь на базовом URL"""
        url = f"{self.base_url}{path}"
        self.driver.get(url)

    def wait_for_element(self, locator):
        """Ожидание появления элемента"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def assert_page_title(self, expected_title):
        """Проверка заголовка страницы"""
        actual_title = self.driver.title
        self.assertEqual(
            actual_title,
            expected_title,
            f"Wrong page title. Expected: {expected_title}, Actual: {actual_title}"
        )

    def switch_on_new_tab(self, main_window):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles if window != main_window][0]
        self.driver.switch_to.window(new_window)
