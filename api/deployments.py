import os
from .auth import AuthorizationObject, BearerToken
import requests
import settings
import logging


logger = logging.getLogger(settings.logName)
AI4EOSC_PAPI_GET_DEPLOYMENTS = '{}/v1/deployments/'
AI4EOSC_PAPI_CREATE_DEPLOYMENT = '{}/v1/deployments/'
AI4EOSC_PAPI_GET_DEPLOYMENT = '{}/v1/deployments/{}'
AI4EOSC_PAPI_DELETE_DEPLOYMENT = '{}/v1/deployments/{}'


def get_deployments(api_url: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_GET_DEPLOYMENTS.format(api_url)
    return requests.get(url, headers=headers)


def get_deployment(api_url: str, deployment_uuid: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_GET_DEPLOYMENT.format(api_url, deployment_uuid)
    return requests.get(url, headers=headers)


def create_deployment(api_url: str, conf: dict, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_CREATE_DEPLOYMENT.format(api_url)
    return requests.post(url, headers=headers, json=conf)


def delete_deployment(api_url: str, deployment_uuid: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_DELETE_DEPLOYMENT.format(api_url, deployment_uuid)
    return requests.delete(url, headers=headers)


if __name__ == '__main__':
    egi_token = os.environ.get(settings.envvar_AI4EOSC_PAPI_TOKEN)
    if (egi_token is None) or (len(egi_token) == 0):
        print(f'No or empty auth token, set env var {settings.envvar_AI4EOSC_PAPI_TOKEN}')
        exit(1)
    auth = BearerToken(egi_token)
    response = get_deployments(settings.AI4EOSC_PAPI_URL, auth)
    print(f'Status: {response.status_code}')
    print(response.text)
