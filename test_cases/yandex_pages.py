from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as webdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from basepage import BasePage


class YandexLocator(object):

    search_input_field = (By.XPATH, '//input[@id="text"]')
    suggest_table = (
        By.CSS_SELECTOR,
        '.mini-suggest__popup.mini-suggest__popup_theme_tile.mini-suggest__popup_visible'
    )


class HomeYandexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_field = self.find_elem(YandexLocator.search_input_field)
        self.suggest_table = None

    def enter_word(self, word):
        return self.search_field.send_keys(word)

    def get_search_field(self):
        return self.search_field

    def get_suggest_table(self):
        self.suggest_table = self.find_elem(YandexLocator.suggest_table)
        return self.suggest_table

    def press_enter(self):
        self.search_field.send_keys(Keys.ENTER)
        return self.search_field

