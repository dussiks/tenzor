from selenium.webdriver.support.wait import WebDriverWait as webdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_elem(self, locator, time=5):
        try:
            element = webdw(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can not find element by locator {locator}"
            )
            return element
        except TimeoutException as e:
            print(e.msg)
            pass

    def find_elems(self, locator, time=5):
        try:
            elements = webdw(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can not find elements by locator {locator}"
            )
            return elements
        except TimeoutException as e:
            print(e.msg)
            pass
