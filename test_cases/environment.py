import unittest

from selenium import webdriver

import print_services as PServ


START_PAGE = 'http://yandex.ru/'


class TestEnvironment(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(START_PAGE)
        self.driver.set_page_load_timeout(10)
        PServ.show_set_up_info('Chrome')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        driver = self.driver
        if driver is not None:
            PServ.show_set_down_info()
            driver.close()
            driver.quit()
