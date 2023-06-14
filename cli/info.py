import typer
import json
import settings
from api.info import get_platform_info, get_api_version_info, get_default_deployment_conf
from api.auth import BearerToken
import logging
import auth


logger = logging.getLogger(settings.logName)
app = typer.Typer(help='Show information about the platform, API or default deployment.')


@app.command()
def default_deployment(
    module_name: str = typer.Argument(None, help="Name of module from which to retrieve default config"),
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    auth_token: str = typer.Option(None, '--auth-token', '-t', help='authorization bearer token', envvar=settings.envvar_AI4EOSC_PAPI_TOKEN),
    oidc_account: str = typer.Option(None, '--oidc-agent-account', help='Account name in oidc-agent', envvar=settings.envvar_OIDC_AGENT_ACCOUNT),
    oidc_token: str = typer.Option(None, '--oidc-access-token', help='OIDC access token', envvar=settings.envvar_OIDC_ACCESS_TOKEN),
    mytoken: str = typer.Option(None, '--mytoken', help='mytoken string', envvar=settings.envvar_AI4EOSC_MYTOKEN),
    mytoken_server: str = typer.Option(None, '--mytoken-server', help='mytoken server URL', envvar=settings.envvar_AI4EOSC_MYTOKEN_SERVER),
):
    if auth_token is None:
        auth_token = auth.get_access_token(oidc_token, oidc_account, mytoken, mytoken_server)
    if auth_token is not None:
        auth_object = BearerToken(auth_token)
    else:
        auth_object = None
    response = get_default_deployment_conf(api_url=api_url, module_name=module_name, auth=auth_object)
    if response is None:
        print('No response')
    elif response.status_code > 299:
        print(f'Error: status code {response.status_code}, {response.text}')
    else:
        info = response.json()
        info_str = json.dumps(info, indent=4)
        print(info_str)


@app.command()
def api_info(
    api_version: str = typer.Option('1', help="API version to get info about"),
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
):
    response = get_api_version_info(api_url, 'v' + api_version)
    if response is None:
        print('No response')
    elif response.status_code > 299:
        print(f'Error: status code {response.status_code}, {response.text}')
    else:
        info = response.json()
        info_str = json.dumps(info, indent=4)
        print(info_str)


@app.command()
def platform_info(api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL)):
    response = get_platform_info(api_url)
    if response is None:
        print('No response')
    elif response.status_code > 299:
        print(f'Error: status code {response.status_code}, {response.text}')
    else:
        info = response.json()
        info_str = json.dumps(info, indent=4)
        print(info_str)
