from typing import List, Dict, Tuple

import requests
from requests import HTTPError

from django.conf import settings

def fetch_data(name: str, url: str, api_key: str) -> Tuple[List[Dict], str | None, int] | Tuple[None, str, int]:
    try:
        response = requests.get(
            f'{url}{api_key}/search/{name}')
        response.raise_for_status()
        if response.json().get('response') == 'success':
            return response.json().get('results'), None, 200
        else:
            error = response.json().get('error')
            return None, error, 404
    except HTTPError as error:
        return None, error.args[0], 500


def main(name: str, url: str = settings.API_BASE_URL, api_key: str = settings.API_KEY):
    response = fetch_data(name, url, api_key)
    print(response)

if __name__ == '__main__':
    main(name='Hulkjkjkjkj')