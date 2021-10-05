from selenium.webdriver.common.by import By

from test_base.base_page import BasePage
from test_base.exceptions import ObjectIsNotFoundOnWebPage


class ImageLocator(object):

    images_categories = (By.CSS_SELECTOR, '.PopularRequestList>div')
    category_url = (By.CSS_SELECTOR, '.PopularRequestList>div>a')
    preview_images = (By.CSS_SELECTOR, '.serp-item__preview')
    image_view = (By.CSS_SELECTOR, '.MMImage-Origin')
    next_button = (
        By.CSS_SELECTOR,
        '.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button'
    )
    previous_button = (
        By.CSS_SELECTOR,
        '.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button'
    )


class YandexImagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.images_categories = self.find_elems(ImageLocator.images_categories)

    def get_images_categories(self):
        return self.images_categories

    def get_image_category_url(self, num: int = 0) -> str:
        """
        Return url for image category. If num argument is not given -
        return url for first category found.
        """

        categories_urls = self.find_elems(ImageLocator.category_url)
        if num < len(categories_urls):
            category_url = categories_urls[num]

            try:
                href = category_url.get_attribute('href')
                return href
            except AttributeError:
                pass

    def get_preview_images(self):
        return self.find_elems(ImageLocator.preview_images)

    def get_preview_image(self, num: int = 0):
        """
        Return src attribute for preview image. If num argument
        is not given - return for first preview image found.
        """

        preview_images = self.find_elems(ImageLocator.preview_images)
        if num < len(preview_images):
            return preview_images[num]

    def get_image_view(self):
        return self.find_elem(ImageLocator.image_view)

    def get_image_view_src(self):
        image = self.get_image_view()

        try:
            source = image.get_attribute('src')
            return source
        except AttributeError:
            pass

    def slide_image_forward(self):
        forward_button = self.find_elem(ImageLocator.next_button)

        try:
            forward_button.click()
        except AttributeError:
            raise ObjectIsNotFoundOnWebPage(
                'forward_button is not found on the web page.'
            )

    def slide_image_backward(self):
        backward_button = self.find_elem(ImageLocator.previous_button)

        try:
            backward_button.click()
        except AttributeError:
            raise ObjectIsNotFoundOnWebPage(
                'backward_button is not found on the web page.'
            )
