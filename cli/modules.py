from api.auth import BearerToken
from api.modules import get_modules_list, get_modules_summary, get_module_metadata, update_module_metadata
from api.tools import show_response
import json


def modules_impl(module_name, api_url, auth_token, summary, update, new_metadata):
    '''
    Accesses the modules interface of AI4EOSC PAPI
    Possible uses:
    <program name> modules - will list modules
    <program name> modules --summary - will provide summary of all modules
    <program name> modules <module name> - will provide info about a module
    <program name> modules <module name> --update --new-metadata <file> - will update module metadata

    :param module_name: name of the module to query or update
    :param api_url: AI4EOSC PAPI URL
    :param auth_token: authorization bearer token
    :param summary: flag indicating that we should provide a summary of modules and not just their listing
    :param update: flag indicating that we're updating module metadata, not querying it
    :param new_metadata: name of file with new metadata
    :return: none
    '''
    if auth_token is not None:
        auth_object = BearerToken(auth_token)
    else:
        auth_object = None
    if (module_name is None) and (not summary) and (not update) and (new_metadata is None):
        #module list
        cli_list_modules(api_url)
    elif (module_name is None) and summary and (not update) and (new_metadata is None):
        #modules summary
        cli_modules_summary(api_url)
    elif (module_name is not None) and (not summary) and (not update) and (new_metadata is None):
        #list module metadata
        cli_show_module(api_url, module_name)
    elif (module_name is not None) and (not summary) and update and (new_metadata is not None):
        #update module metadata
        cli_update_module(api_url, module_name, new_metadata)
    else:
        print('Error: incorrect combination of options and arguments')


def cli_list_modules(api_url):
    response = get_modules_list(api_url)
    show_response(response)



def cli_modules_summary(api_url):
    response = get_modules_summary(api_url)
    show_response(response)


def cli_show_module(api_url, module_name):
    response = get_module_metadata(api_url, module_name)
    show_response(response)



def cli_update_module(api_url, module_name, new_metadata):
    nm_dict = None
    try:
        with open(new_metadata, 'rt') as nm_file:
            nm_json = nm_file.read()
            nm_dict = json.loads(nm_json)
    except Exception as e:
        print(f'Error: {str(e)}')
        return

    response = update_module_metadata(api_url, module_name, nm_dict)
    show_response(response)




