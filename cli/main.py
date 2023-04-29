#todo Pouzivaj jednoduchy config subor pre default hodnot (PAPI endpoint, vo, oidc-agent konto, ..). Priority: default hodnoty v kode < default hodnoty v config subor < hodnoty parametrov nastavene v envvar < hodnoty parametrov zadane cez command-line. Neurobil som to pre fedcloudclient od zaciatku a teraz tazko upravujem.
#todo Pouzvaj log file pre debug informacie. Dhlsie chybove spravy sa nedaju citat na konzole. V pripade staci nastavit log_file = stderr. To tiez nemam urobene pre fedcloudclient.
import json

import typer
import settings
from api.info import get_platform_info, get_api_version_info, get_default_deployment_conf
from api.auth import BearerToken

app = typer.Typer()

@app.command()
def info(object: str = typer.Argument(default=None, help='module name for its default config, v=<number> for info about API version, or nothing for info about the platform')):
    response = None
    if not object:
        response = get_platform_info(settings.AI4EOSC_PAPI_URL)
    elif object.startswith("v="):
        response = get_api_version_info(settings.AI4EOSC_PAPI_URL, object[2:])
    else:
        response = get_default_deployment_conf(
            api_url=settings.AI4EOSC_PAPI_V1_URL,
            module_name=object,
            auth=BearerToken('$$$token$$$'))

    if not response:
        print('No response')
    elif response.status_code > 299:
        print(f'Error: status code {response.status_code}')
    else:
        info = response.json()
        info_str = json.dumps(info, indent=4)
        print(info_str)


@app.command()
def modules(module_name: str):
    ...

@app.command()
def deployments(deployment_uuid: str):
    ...

if __name__ == "__main__":
    app()