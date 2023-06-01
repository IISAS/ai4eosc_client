import settings
import requests
import logging


logger = logging.getLogger(settings.logName)
AI4EOSC_PAPI_GET_MODULES_LIST = '{}/v1/modules'
AI4EOSC_PAPI_GET_MODULES_SUMMARY = '{}/v1/modules/summary'
AI4EOSC_PAPI_GET_MODULE_METADATA = '{}/v1/modules/metadata/{}'
AI4EOSC_PAPI_UPDATE_MODULE_METADATA = '{}/v1/modules/metadata/{}'


def get_modules_list(api_url: str):
    url = AI4EOSC_PAPI_GET_MODULES_LIST.format(api_url)
    return requests.get(url)


def get_modules_summary(api_url: str):
    url = AI4EOSC_PAPI_GET_MODULES_SUMMARY.format(api_url)
    return requests.get(url)


def get_module_metadata(api_url: str, module_name: str):
    url = AI4EOSC_PAPI_GET_MODULE_METADATA.format(api_url, module_name)
    return requests.get(url)


def update_module_metadata(api_url: str, module_name: str, new_metadata: dict):
    url = AI4EOSC_PAPI_UPDATE_MODULE_METADATA.format(api_url, module_name)
    return requests.put(url, json=new_metadata)


if __name__ == '__main__':
    mm = get_module_metadata(settings.AI4EOSC_PAPI_URL, 'DEEP-OC-dogs_breed_det').json()
    response = update_module_metadata(settings.AI4EOSC_PAPI_URL, 'DEEP-OC-dogs_breed_det', mm)
    print(f'Status: {response.status_code}')
    print(response.text)
