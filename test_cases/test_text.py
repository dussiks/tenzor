import unittest

import test_base.print_services as PServ
from test_base.environment import TestEnvironment
from test_base.exceptions import ObjectIsNotFoundOnWebPage
from test_base.home_page import YandexHomePage
from test_base.search_page import YandexSearchPage


SEARCH_WORD = 'тензор'
SEARCH_URL = 'tensor.ru'
TOP_RANGE = 5


class TextSearchTest(TestEnvironment):

    def test_text_search_case(self):
        """Tests cases with entered word in Yandex search engine."""

        driver = self.driver
        homepage = YandexHomePage(driver)
        input_field = homepage.search_field

        self.assertIsNotNone(
            input_field,
            msg='None вместо объекта - поисковая строка не найдена.'
        )
        PServ.show_text_test_case_succeeded('input_search_field')

        input_field.clear()
        homepage.enter_word(SEARCH_WORD)
        suggest_table = homepage.get_suggest_table()
        self.assertIsNotNone(
            suggest_table,
            msg='None вместо предложений - таблица вариантов не найдена.'
        )
        PServ.show_text_test_case_succeeded('suggest_table')

        homepage.press_enter()

        search_page = YandexSearchPage(driver)  # new class for new page with search results
        table_with_search_results = search_page.get_search_result_table()
        self.assertIsNotNone(
            table_with_search_results,
            msg='None вместо результатов поиска - таблица не обнаружена.'
        )
        PServ.show_text_test_case_succeeded('table_with_search_results')

        result_links = search_page.get_result_links()

        if result_links is None:
            raise ObjectIsNotFoundOnWebPage(
                'Search results table has no links.'
            )

        self.assertGreater(
            len(result_links),
            0,
            msg='В результатах поиска нет предлагаемых вариантов.')
        PServ.show_text_test_case_succeeded('result_links')

        expected_link = SEARCH_URL
        expected_link_found = False

        for variant in result_links:
            item_link = variant.get_attribute('href')

            for i in range(TOP_RANGE):
                if expected_link in item_link:  # item_link could be with params added by yandex
                    expected_link_found = True

        self.assertTrue(
            expected_link_found,
            msg=f'{expected_link} is not in search results table.'
        )
        PServ.show_text_test_case_succeeded('looking_for_link')


if __name__ == "__main__":
    unittest.main()
