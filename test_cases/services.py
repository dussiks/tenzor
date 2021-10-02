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

