from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from basepage import BasePage


class YandexLocator(object):

    search_input_field = (By.XPATH, '//input[@id="text"]')
    suggest_table = (
        By.CSS_SELECTOR,
        '.mini-suggest__popup.mini-suggest__popup_theme_tile.mini-suggest__popup_visible'
    )
    search_result_table = (By.XPATH, '//ul[@id="search-result"]')
    result_links = (By.CSS_SELECTOR, '#search-result>li>div>h2>a')


class HomeYandexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_field = self.find_elem(YandexLocator.search_input_field)

    def enter_word(self, word):
        return self.search_field.send_keys(word)

    def press_enter(self):
        self.search_field.send_keys(Keys.ENTER)
        return self.search_field

    def get_search_field(self):
        return self.search_field

    def get_suggest_table(self):
        return self.find_elem(YandexLocator.suggest_table)

    def get_search_result_table(self):
        return self.find_elem(YandexLocator.search_result_table, time=15)

    def get_result_links(self):
        return self.find_elems(YandexLocator.result_links)
