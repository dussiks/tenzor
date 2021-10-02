import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import services
from yandex_pages import HomeYandexPage, YandexLocator


START_PAGE = 'http://yandex.ru/'
TEST_DRIVER = 'Chrome'


class TenzorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get(START_PAGE)
        cls.driver.set_page_load_timeout(10)
        services.show_set_up_info(TEST_DRIVER)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        driver = TenzorTest.driver
        if driver is not None:
            services.show_set_down_info()
            driver.close()
            driver.quit()

    def test_search_input_field_observed(self):
        """Checks if input search field is present on web page."""
        driver = TenzorTest.driver
        page = HomeYandexPage(driver)
        input_field = page.get_search_field()

        self.assertNotEqual(
            input_field,
            None,
            msg='None вместо объекта - поисковая строка не найдена.'
        )

    def test_suggest_table_is_shown(self):
        """
        Checks if suggestion list obtained for entered word in search field.
        """
        driver = TenzorTest.driver
        page = HomeYandexPage(driver)
        page.search_field.clear()
        page.enter_word('тензор')
        suggest_table = page.get_suggest_table()
        self.assertNotEqual(
            suggest_table,
            None,
            msg='None вместо предложений - таблица вариантов не найдена.'
        )

    # def test_search_results_page_is_shown(self):
    #     driver = TenzorTest.driver
    #     page = HomeYandexPage(driver)
    #     page.search_field.clear()
    #     page.enter_word('тензор')
    #     page.press_enter()





if __name__ == "__main__":
    unittest.main()
