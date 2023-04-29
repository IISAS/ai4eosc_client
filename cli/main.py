#todo Pouzivaj jednoduchy config subor pre default hodnot (PAPI endpoint, vo, oidc-agent konto, ..). Priority: default hodnoty v kode < default hodnoty v config subor < hodnoty parametrov nastavene v envvar < hodnoty parametrov zadane cez command-line. Neurobil som to pre fedcloudclient od zaciatku a teraz tazko upravujem.
#todo Pouzvaj log file pre debug informacie. Dhlsie chybove spravy sa nedaju citat na konzole. V pripade staci nastavit log_file = stderr. To tiez nemam urobene pre fedcloudclient.
import json

import typer
import settings
from api.info import get_platform_info, get_api_version_info, get_default_deployment_conf
from api.auth import BearerToken

from info import info_impl

app = typer.Typer()

@app.command()
def info(
        object: str = typer.Argument(default=None, help='module name for its default config, v=<number> for info about API version, or nothing for info about the platform'),
        auth_token: str = typer.Option(default=None, help='authorization bearer token')
        ):
    return info_impl(object, auth_token)


@app.command()
def modules(module_name: str):
    ...

@app.command()
def deployments(deployment_uuid: str):
    ...

if __name__ == "__main__":
    app()