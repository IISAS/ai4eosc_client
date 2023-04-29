import json
import settings
from api.info import get_platform_info, get_api_version_info, get_default_deployment_conf
from api.auth import BearerToken


def info_impl(object, auth_token):
    response = None
    if not object:
        response = get_platform_info(settings.AI4EOSC_PAPI_URL)
    elif object.startswith("v="):
        response = get_api_version_info(settings.AI4EOSC_PAPI_URL, 'v'+object[2:])
    else:
        response = get_default_deployment_conf(
            api_url=settings.AI4EOSC_PAPI_V1_URL,
            module_name=object,
            auth=BearerToken(auth_token))

    if response is None:
        print('No response')
    elif response.status_code > 299:
        print(f'Error: status code {response.status_code}, {response.text}')
    else:
        info = response.json()
        info_str = json.dumps(info, indent=4)
        print(info_str)