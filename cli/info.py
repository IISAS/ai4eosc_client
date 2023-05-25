import typer
import json
import settings
from api.info import get_platform_info, get_api_version_info, get_default_deployment_conf
from api.auth import BearerToken

app = typer.Typer()

@app.command()
def default_deployment(
        module_name: str = typer.Argument(
            None,
            help="Name of module from which to retrieve default config"
        ),
        api_url: str = typer.Option(
            settings.AI4EOSC_PAPI_URL,
            help="AI4EOSC PAPI URL",
            envvar=settings.envvar_AI4EOSC_PAPI_URL),
        auth_token: str = typer.Option(
            None,
            '--auth-token', '-t',
            help='authorization bearer token',
            envvar=settings.envvar_AI4EOSC_PAPI_TOKEN)
        ):
    response = get_default_deployment_conf(
        api_url=api_url,
        module_name=module_name,
        auth=BearerToken(auth_token))

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
        api_version: str = typer.Option(
            '1',
            help="API version to get info about"
        ),
        api_url: str = typer.Option(
            settings.AI4EOSC_PAPI_URL,
            help="AI4EOSC PAPI URL",
            envvar=settings.envvar_AI4EOSC_PAPI_URL)
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
def platform_info(
        api_url: str = typer.Option(
            settings.AI4EOSC_PAPI_URL,
            help="AI4EOSC PAPI URL",
            envvar=settings.envvar_AI4EOSC_PAPI_URL)
):
    response = get_platform_info(api_url)
    if response is None:
        print('No response')
    elif response.status_code > 299:
        print(f'Error: status code {response.status_code}, {response.text}')
    else:
        info = response.json()
        info_str = json.dumps(info, indent=4)
        print(info_str)
