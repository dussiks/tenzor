import unittest

import print_services as PServ
from environment import TestEnvironment
from yandex_pages import HomeYandexPage


class TenzorTest(TestEnvironment):

    def test_tenzor_search_case(self):
        """Tests cases with entered word in given search engine."""

        driver = self.driver
        page = HomeYandexPage(driver)
        input_field = page.get_search_field()

        self.assertNotEqual(
            input_field,
            None,
            msg='None вместо объекта - поисковая строка не найдена.'
        )
        PServ.show_test_case_succeeded('input_search_field')

        page.search_field.clear()
        page.enter_word('тензор')
        suggest_table = page.get_suggest_table()
        self.assertIsNotNone(
            suggest_table,
            msg='None вместо предложений - таблица вариантов не найдена.'
        )
        PServ.show_test_case_succeeded('suggest_table')

        page.press_enter()
        table_with_search_results = page.get_search_result_table()
        self.assertIsNotNone(
            table_with_search_results,
            msg='None вместо результатов поиска - таблица не обнаружена.'
        )
        PServ.show_test_case_succeeded('table_with_search_results')

        result_links = page.get_result_links()
        self.assertGreater(
            len(result_links),
            0,
            msg='В результатах поиска нет предлагаемых вариантов.')
        PServ.show_test_case_succeeded('result_links')

        looking_for_link = 'tensor.ru'
        looking_for_link_found = False

        for variant in result_links:
            item_link = variant.get_attribute('href')

            for i in range(5):
                if looking_for_link in item_link:
                    looking_for_link_found = True

        self.assertTrue(
            looking_for_link_found,
            msg=f'{looking_for_link} is not in search results table.'
        )
        PServ.show_test_case_succeeded('looking_for_link')


if __name__ == "__main__":
    unittest.main()
