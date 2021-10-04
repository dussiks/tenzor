from selenium.webdriver.common.by import By

from test_base.base_page import BasePage


class ImageLocator(object):

    images_categories = (By.CSS_SELECTOR, '.PopularRequestList>div')
    category_url = (By.CSS_SELECTOR, '.PopularRequestList>div>a')


class YandexImagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_images_categories(self):
        return self.find_elems(ImageLocator.images_categories)

    def get_image_category_url(self, num: int = 0):
        categories_urls = self.find_elems(ImageLocator.category_url)
        if num < len(categories_urls):
            category_url = categories_urls[num]

            try:
                href = category_url.get_attribute('href')
                return href
            except AttributeError:
                return



