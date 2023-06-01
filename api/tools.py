from urllib.parse import urlencode
from requests import Response
import json
import settings
import logging


logger = logging.getLogger(settings.logName)


def encode_url(url, **kwargs):
    """
    Encode a URL with parameters
    :param url: the base URL
    :param kwargs: an arbitrary dictionary of keys and values which will be encoded in key=value form into the URL
    :return: a fully encoded URL usable for HTTP.GET
    """
    return f'{url}?{urlencode(kwargs)}'


def show_response(response: Response):
    if response is None:
        print('No response')
    elif response.status_code > 299:
        print(f'Error: status code {response.status_code}, {response.text}')
    else:
        info = response.json()
        info_str = json.dumps(info, indent=4)
        print(info_str)


if __name__ == '__main__':
    print(encode_url(url='http://1.2.3/v4', param1='1', param2='dva a dva'))
