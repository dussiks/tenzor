from datetime import datetime


def show_set_up_info(test_driver=None) -> None:
    """Prints additional info to console about test driver set up."""

    print(f'Started at: {datetime.now()}')
    print(f'{test_driver} driver environment set up.')
    print('----------------------------------------------------------')


def show_set_down_info() -> None:
    """Prints additional info to console about test driver shut down."""

    print('----------------------------------------------------------')
    print(f'Test environment destroyed. Driver will be shut down.')
    print(f'Run completed at: {datetime.now()}')


def show_test_case_succeeded(test_condition) -> None:
    """Prints to console success statuses for received test case."""

    test_cases_success_outputs = {
        'input_search_field': 'Input search field found. OK.',
        'suggest_table': 'Table with suggestions for searching found. OK.',
        'table_with_search_results': 'Table with results found. OK.',
        'result_links': 'Search results have variants. OK.',
        'looking_for_link': 'Looking for link found in given range. OK.'
    }
    print(test_cases_success_outputs[test_condition])
