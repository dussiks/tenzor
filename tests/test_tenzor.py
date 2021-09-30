import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TenzorSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_yandex_logo(self):
        driver = self.driver
        driver.get('https://yandex.ru')
        self.assertEqual(driver.title.lower(), 'яндекс')

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

