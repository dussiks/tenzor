import re
from urllib.parse import unquote


def get_image_search_text(search_url: str) -> str:
    """Decode url string and get text query parameter value."""

    full_url = unquote(search_url)
    query_param = 'text='
    match = re.search(query_param, full_url)

    if match is not None:
        start_idx, end_idx = match.span()
        url_params_part = full_url[end_idx:]
        end_symbol = '&'
        end_symbol_idx = url_params_part.index(end_symbol)
        search_text = url_params_part[:end_symbol_idx]

        return search_text

