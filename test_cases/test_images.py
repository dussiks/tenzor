import unittest

import test_base.print_services as PServ
from test_base.environment import TestEnvironment
from test_base.exceptions import ObjectIsNotFoundOnWebPage
from test_base.home_page import YandexHomePage
from test_base.image_page import YandexImagePage
from test_base.utils import get_image_search_text


class YandexImage(TestEnvironment):

    def test_yandex_image_case(self):
        """Tests cases with images block in given search engine."""

        driver = self.driver
        homepage = YandexHomePage(driver)
        yandex_images = homepage.get_images_block()

        if yandex_images is None:
            raise ObjectIsNotFoundOnWebPage(
                'Yandex image block is not found.'
            )

        expected_text = 'Картинки'
        self.assertEqual(
            expected_text.lower(),
            yandex_images.text.lower(),
            msg=f'Название выбранного блока на сайте'
                f'отличается от ожидаемого: {expected_text}'
        )
        PServ.show_image_test_case_succeeded('image_block')
        yandex_images.click()
        homepage.change_to_second_tab()

        image_page = YandexImagePage(driver)  # new class for page with images
        page_url = image_page.get_page_url()
        expected_url = 'https://yandex.ru/images/'
        self.assertIn(
            expected_url,
            page_url,
            msg=f'Искомый адрес: {expected_url} не найден в адресе сайта.'
        )
        PServ.show_image_test_case_succeeded('new_tab_url')

        images_categories = image_page.get_images_categories()

        if len(images_categories) < 1:
            raise ObjectIsNotFoundOnWebPage(
                'No image categories found on web page.'
            )

        first_category = images_categories[0]
        first_category_url = image_page.get_image_category_url()
        first_category.click()
        new_page_url = image_page.get_page_url()
        self.assertEqual(
            first_category_url,
            new_page_url,
            msg=f'Opened page url: {new_page_url}.'
                f'Expected url: {first_category_url}'
        )
        PServ.show_image_test_case_succeeded('new_page_url')

        expected_text = first_category.text
        current_url = image_page.get_page_url()
        image_search_text = get_image_search_text(current_url)
        self.assertEqual(
            expected_text,
            image_search_text,
            msg=f'Text in search input: {image_search_text} is not'
                f'as expected: {expected_text}'
        )
        PServ.show_image_test_case_succeeded('image_search_text')




if __name__ == "__main__":
    unittest.main()
