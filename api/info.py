from api.auth import BearerToken, AuthorizationObject
import settings
import requests
import os

AI4EOSC_PAPI_GET_DEFAULT_DEPLOYMENT_CONF='{}/v1/info/conf/{}'
AI4EOSC_PAPI_GET_PLATFORM_INFO='{}'
AI4EOSC_PAPI_GET_API_VERSION_INFO='{}/{}'

def get_default_deployment_conf(api_url: str, module_name: str, auth: AuthorizationObject):
    url=AI4EOSC_PAPI_GET_DEFAULT_DEPLOYMENT_CONF.format(api_url, module_name)
    headers = auth.apply_authorization()
    return requests.get(url, headers=headers)


def get_platform_info(api_url: str):
    url=AI4EOSC_PAPI_GET_PLATFORM_INFO.format(api_url)
    return requests.get(url)


def get_api_version_info(api_url: str, version: str):
    url=AI4EOSC_PAPI_GET_API_VERSION_INFO.format(api_url, version)
    return requests.get(url)


if __name__ == '__main__':
    response = get_platform_info(settings.AI4EOSC_PAPI_URL)
    print(f'Status: {response.status_code}')
    print(response.text)
    response = get_api_version_info(settings.AI4EOSC_PAPI_URL, 'v1')
    print(f'Status: {response.status_code}')
    print(response.text)
    egi_token = os.environ.get(settings.envvar_AI4EOSC_PAPI_TOKEN)
    if (egi_token is None) or (len(egi_token) == 0):
        print(f'No or empty auth token, set env var {settings.envvar_AI4EOSC_PAPI_TOKEN}')
        exit(1)
    auth = BearerToken(egi_token)
    response = get_default_deployment_conf(settings.AI4EOSC_PAPI_V1_URL, 'DEEP-OC-dogs_breed_det', auth)
    print(f'Status: {response.status_code}')
    print(response.text)



