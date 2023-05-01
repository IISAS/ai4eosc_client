import json

from api.auth import BearerToken
from api.deployments import get_deployments, get_deployment, create_deployment, delete_deployment
from api.tools import show_response


def deployments_impl(
        deployment_uuid: str,
        api_url: str,
        auth_token: str,
        create: bool,
        delete: bool,
        new_deployment: str):
    '''
    Accesses the deployments interface of AI4EOSC PAPI
    Possible uses:
    <program name> deployments - will list deployments
    <program name> deployments uudi - will provide info about a deployment
    <program name> deployments --delete uuid - will delete a deployment
    <program name> deployments --create --new-deployment <file> - will create a new deployment based on the provided file

    :param deployment_uuid: deployment UUID
    :param api_url: AI4EOSC PAPI URL
    :param auth_token: authorization token
    :param create: flag saying that we're creating new deployment (in that case @new_deployment is also needed)
    :param delete: flag that we're deleting a deployment
    :param new_deployment: file with information about new deployment
    :return: nothing
    '''
    if auth_token is not None:
        auth_object = BearerToken(auth_token)
    else:
        auth_object = None
    if (deployment_uuid is None) and (not create) and (not delete) and (new_deployment is None):
        #list deployments
        cli_list_deployments(api_url, auth_object)
    elif (deployment_uuid is not None) and (not create) and (not delete) and (new_deployment is None):
        #show deployment info
        cli_show_deployment(deployment_uuid, api_url, auth_object)
    elif (deployment_uuid is not None) and delete and (not create) and (new_deployment is None):
        #delete deployment
        cli_delete_deployment(deployment_uuid, api_url, auth_object)
    elif (deployment_uuid is None) and create and (not delete) and (new_deployment is not None):
        #create deployment
        cli_create_deployment(api_url, auth_object, new_deployment)
    else:
        print('Error: incorrect combination of options and arguments')


def cli_list_deployments(api_url, auth_object):
    response = get_deployments(api_url, auth_object)
    show_response(response)


def cli_show_deployment(deployment_uuid, api_url, auth_object):
    response = get_deployment(api_url, deployment_uuid, auth_object)
    show_response(response)


def cli_delete_deployment(deployment_uuid, api_url, auth_object):
    response = delete_deployment(api_url, deployment_uuid, auth_object)
    show_response(response)

def cli_create_deployment(api_url, auth_object, deployment_def):
    dd_dict = None
    try:
        with open(deployment_def, 'rt') as dd_file:
            dd_json = dd_file.read()
            dd_dict = json.loads(dd_json)
    except Exception as e:
        print(f'Error: {str(e)}')
        return

    response = create_deployment(api_url, dd_dict, auth_object)
    show_response(response)