import hashlib
import os
import re
import urllib.request
from urllib.parse import unquote


def get_image_search_text(search_url: str) -> str:
    """Decode url string and get text query parameter value."""

    try:
        full_url = unquote(search_url)
    except TypeError:
        return

    query_param = 'text='
    match = re.search(query_param, full_url)

    if match is not None:
        start_idx, end_idx = match.span()
        url_params_part = full_url[end_idx:]
        end_symbol = '&'
        end_symbol_idx = url_params_part.index(end_symbol)
        search_text = url_params_part[:end_symbol_idx]

        return search_text


def hash_object(path):
    with open(path, 'rb') as file:
        hasher = hashlib.md5()
        hasher.update(file.read())
        return hasher.hexdigest()


def get_hashed_image(url: str, image_name: str, download_folder: str) -> str:
    """Return image as a hashed string."""

    directory_name = get_directory_path_or_none(download_folder)
    new_image_name = f'{directory_name}/{image_name}'

    if download_image_and_return_result(url, new_image_name):
        hash_name = hash_object(new_image_name)
        return hash_name


def get_directory_path_or_none(directory_name):
    """
    Return full path for the given folder. Folder is looked for
    in current directory.
    """

    if create_directory_and_return_result(directory_name):
        try:
            current_path = os.getcwd()
        except OSError:
            return

        folder_path = f'{current_path}/{directory_name}'
        return folder_path


def create_directory_and_return_result(folder_name: str) -> bool:
    """
    Create new directory in current directory if it does not exist and
    return final True if directory exist/created or False. 
    """

    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            return True
        except OSError as e:
            pass

    return True


def download_image_and_return_result(image_url: str, image_name: str) -> bool:
    """
    Download file from given url and naming it with given full name.
    Return bool for succeeding.
    """
    try:
        urllib.request.urlretrieve(image_url, image_name)
        return True
    except Exception:
        pass
