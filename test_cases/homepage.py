from selenium.webdriver.common.by import By

from locators import Locator


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.search_input_fields = driver.find_elements(
            By.XPATH,
            Locator.search_input_field
        )

    def get_search_input_field(self):
        return self.search_input_fields
