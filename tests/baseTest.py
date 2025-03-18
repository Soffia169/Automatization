import time
import unittest
import os
import shutil
import uuid

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseSeleniumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = "https://sbis.ru"
        cls.browser = 'chrome'
        cls.headless = False

    def setUp(self):
        self._init_driver()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def _init_driver(self):
        if self.browser == 'chrome':
            from selenium.webdriver.chrome.options import Options
            options = Options()
            if self.headless:
                options.add_argument("--headless=new")
            options.add_argument("--disable-safe-browsing")

            download_path = os.path.join(os.path.dirname(__file__), "downloads")
            shutil.rmtree(download_path, ignore_errors=True)
            os.makedirs(download_path, exist_ok=True)

            options.add_experimental_option('prefs', {
                "download.default_directory": download_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
                "browser.download.folderList": 2,
                "browser.download.manager.showWhenStarting": False,
                "browser.helperApps.neverAsk.saveToDisk": "exe"
            })
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
        screenshot_name = f'{self._testMethodName}_{str(uuid.uuid4())}'
        png_bytes = self.driver.get_screenshot_as_png()
        allure.attach(
            png_bytes,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )

    def switch_on_new_tab(self, main_window):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles if window != main_window][0]
        self.driver.switch_to.window(new_window)

    def wait_for_download(self, directory, timeout=30):
        end_time = time.time() + timeout
        while True:
            temp_files = [f for f in os.listdir(directory) if f.endswith('.crdownload')]
            exe_files = [f for f in os.listdir(directory) if f.endswith('.exe')]
            if not temp_files and exe_files:
                return exe_files[0]
            if time.time() > end_time:
                raise TimeoutError("Файл не загрузился за отведенное время")
            time.sleep(1)