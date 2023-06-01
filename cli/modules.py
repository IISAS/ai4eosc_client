from api.modules import get_modules_list, get_modules_summary, get_module_metadata, update_module_metadata
from api.tools import show_response
import json, typer, settings
import logging


logger = logging.getLogger(settings.logName)
app = typer.Typer()


@app.command()
def list_modules(api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL)):
    cli_list_modules(api_url)


@app.command()
def modules_summary(api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL)):
    cli_modules_summary(api_url)


@app.command()
def show_module(
    module_name: str = typer.Option(None, help='module name to query'),
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
):
    cli_show_module(api_url, module_name)


@app.command()
def update_module(
    module_name: str = typer.Option(None, help='module name to query'),
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    new_metadata: str = typer.Option(None, '--new-metadata', '-nm', help='name of JSON file with new metadata'),
):
    cli_update_module(api_url, module_name, new_metadata)


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
