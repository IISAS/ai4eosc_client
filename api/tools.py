from urllib.parse import urlencode

def encode_url(url, **kwargs):
    '''
    Encode a URL with parameters
    :param url: the base URL
    :param kwargs: an arbitrary dictionary of keys and values which will be encoded in key=value form into the URL
    :return: a fully encoded URL usable for HTTP.GET
    '''
    return f'{url}?{urlencode(kwargs)}'

if __name__ == '__main__':
    print(encode_url(url='http://1.2.3/v4', param1='1', param2='dva a dva'))