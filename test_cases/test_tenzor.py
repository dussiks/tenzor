import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import services
from homepage import HomePage


START_PAGE = 'http://yandex.ru/'
TEST_DRIVER = 'Chrome'


class TenzorTest(unittest.TestCase):
    DRIVERS = {
        'Chrome': webdriver.Chrome,
        'Firefox': webdriver.Firefox
    }

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = cls.DRIVERS.get(TEST_DRIVER)()
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

    def test_yandex_page_is_opened(self):
        driver = TenzorTest.driver
        expected_title = 'Яндекс'
        self.assertEqual(
            driver.title,
            expected_title,
            msg='Загруженная страница не является поисковиком Яндекс.'
        )

    def test_search_input_field_observed(self):
        driver = TenzorTest.driver
        page = HomePage(driver)
        search_fields = page.get_search_input_field()

        self.assertEqual(
            1,
            len(search_fields),
            msg=f'Не удалось обнаружить строку поиска на ресурсе: {START_PAGE}'
        )




if __name__ == "__main__":
    unittest.main()
