import typer
import json
from api.auth import BearerToken
from api.deployments import get_deployments, get_deployment, create_deployment, delete_deployment
from api.tools import show_response
import settings
import logging
from typing import List
import auth


logger = logging.getLogger(settings.logName)
app = typer.Typer(help='Access deployments - list existing, show their info, create new or delete existing.')


@app.command()
def list(
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    auth_token: str = typer.Option(None, '--auth-token', '-t', help='authorization bearer token', envvar=settings.envvar_AI4EOSC_PAPI_TOKEN),
    vos: List[str] = typer.Option(None, '--vo', help='user\'s vo to use, can be used multiple times'),
    oidc_account: str = typer.Option(None, '--oidc-agent-account', help='Account name in oidc-agent', envvar=settings.envvar_OIDC_AGENT_ACCOUNT),
    mytoken: str = typer.Option(None, '--mytoken', help='mytoken string', envvar=settings.envvar_AI4EOSC_MYTOKEN),
    mytoken_server: str = typer.Option(None, '--mytoken-server', help='mytoken server URL', envvar=settings.envvar_AI4EOSC_MYTOKEN_SERVER),
):
    if auth_token is None:
        auth_token = auth.get_access_token(oidc_account, mytoken, mytoken_server)
    if auth_token is not None:
        auth_object = BearerToken(auth_token)
    else:
        auth_object = None
    response = get_deployments(api_url, auth_object, vos)
    show_response(response)


@app.command()
def show(
    deployment_uuid: str = typer.Argument(None, help='deployment UUID'),
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    auth_token: str = typer.Option(None, '--auth-token', '-t', help='authorization bearer token', envvar=settings.envvar_AI4EOSC_PAPI_TOKEN),
    oidc_account: str = typer.Option(None, '--oidc-agent-account', help='Account name in oidc-agent', envvar=settings.envvar_OIDC_AGENT_ACCOUNT),
    mytoken: str = typer.Option(None, '--mytoken', help='mytoken string', envvar=settings.envvar_AI4EOSC_MYTOKEN),
    mytoken_server: str = typer.Option(None, '--mytoken-server', help='mytoken server URL', envvar=settings.envvar_AI4EOSC_MYTOKEN_SERVER),
):
    if auth_token is None:
        auth_token = auth.get_access_token(oidc_account, mytoken, mytoken_server)
    if auth_token is not None:
        auth_object = BearerToken(auth_token)
    else:
        auth_object = None
    response = get_deployment(api_url, deployment_uuid, auth_object)
    show_response(response)


@app.command()
def create(
    new_deployment: str = typer.Option(None, '--new-deployment', '-nd', help='name of JSON file with new deployment specification'),
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    auth_token: str = typer.Option(None, '--auth-token', '-t', help='authorization bearer token', envvar=settings.envvar_AI4EOSC_PAPI_TOKEN),
    vo: str = typer.Option(None, '--vo', help='name of the VO for the new deployment', envvar=settings.envvar_AI4EOSC_DEFAULT_VO),
    oidc_account: str = typer.Option(None, '--oidc-agent-account', help='Account name in oidc-agent', envvar=settings.envvar_OIDC_AGENT_ACCOUNT),
    mytoken: str = typer.Option(None, '--mytoken', help='mytoken string', envvar=settings.envvar_AI4EOSC_MYTOKEN),
    mytoken_server: str = typer.Option(None, '--mytoken-server', help='mytoken server URL', envvar=settings.envvar_AI4EOSC_MYTOKEN_SERVER),
):
    if auth_token is None:
        auth_token = auth.get_access_token(oidc_account, mytoken, mytoken_server)
    if auth_token is not None:
        auth_object = BearerToken(auth_token)
    else:
        auth_object = None
    try:
        with open(new_deployment, 'rt') as dd_file:
            dd_json = dd_file.read()
            dd_dict = json.loads(dd_json)
            response = create_deployment(api_url, dd_dict, auth_object, vo)
            show_response(response)
    except Exception as e:
        print(f'Error: {str(e)}')
        return


@app.command()
def delete(
    deployment_uuid: str = typer.Argument(None, help='deployment UUID'),
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    auth_token: str = typer.Option(None, '--auth-token', '-t', help='authorization bearer token', envvar=settings.envvar_AI4EOSC_PAPI_TOKEN),
    vo: str = typer.Option(None, '--vo', help='name of the VO where the deployment is located', envvar=settings.envvar_AI4EOSC_DEFAULT_VO),
    oidc_account: str = typer.Option(None, '--oidc-agent-account', help='Account name in oidc-agent', envvar=settings.envvar_OIDC_AGENT_ACCOUNT),
    mytoken: str = typer.Option(None, '--mytoken', help='mytoken string', envvar=settings.envvar_AI4EOSC_MYTOKEN),
    mytoken_server: str = typer.Option(None, '--mytoken-server', help='mytoken server URL', envvar=settings.envvar_AI4EOSC_MYTOKEN_SERVER),
):
    if auth_token is None:
        auth_token = auth.get_access_token(oidc_account, mytoken, mytoken_server)
    if auth_token is not None:
        auth_object = BearerToken(auth_token)
    else:
        auth_object = None
    response = delete_deployment(api_url, deployment_uuid, auth_object, vo)
    show_response(response)
