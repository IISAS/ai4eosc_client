from api.modules import get_modules_list, get_modules_summary, get_module_metadata, update_module_metadata, get_tags
from api.tools import show_response
import json, typer, settings
import logging
from typing import List, Optional


logger = logging.getLogger(settings.logName)
app = typer.Typer(help="Access modules - list them, show their summary, list existing tags, show or update module metadata.")


@app.command()
def list_modules(
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    tags: Optional[List[str]] = typer.Option(None, '--tags'),
    tags_any: Optional[List[str]] = typer.Option(None, '--tags-any'),
    not_tags: Optional[List[str]] = typer.Option(None, '--not-tags'),
    not_tags_any: Optional[List[str]] = typer.Option(None, '--not-tags-any'),
):
    split_tags = []
    for tag in tags:
        split_tags.extend(tag.split(','))
    split_tags_any = []
    for tag in tags_any:
        split_tags_any.extend(tag.split(','))
    split_not_tags = []
    for tag in not_tags:
        split_not_tags.extend(tag.split(','))
    split_not_tags_any = []
    for tag in not_tags_any:
        split_not_tags_any.extend(tag.split(','))
    cli_list_modules(api_url, split_tags, split_tags_any, split_not_tags, split_not_tags_any)


@app.command()
def modules_summary(
    api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL),
    tags: Optional[List[str]] = typer.Option(None, '--tags'),
    tags_any: Optional[List[str]] = typer.Option(None, '--tags-any'),
    not_tags: Optional[List[str]] = typer.Option(None, '--not-tags'),
    not_tags_any: Optional[List[str]] = typer.Option(None, '--not-tags-any'),
):
    split_tags = []
    for tag in tags:
        split_tags.extend(tag.split(','))
    split_tags_any = []
    for tag in tags_any:
        split_tags_any.extend(tag.split(','))
    split_not_tags = []
    for tag in not_tags:
        split_not_tags.extend(tag.split(','))
    split_not_tags_any = []
    for tag in not_tags_any:
        split_not_tags_any.extend(tag.split(','))
    cli_modules_summary(api_url, split_tags, split_tags_any, split_not_tags, split_not_tags_any)


@app.command()
def tags(api_url: str = typer.Option(settings.AI4EOSC_PAPI_URL, help="AI4EOSC PAPI URL", envvar=settings.envvar_AI4EOSC_PAPI_URL)):
    cli_tags(api_url)


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


def cli_list_modules(api_url, tags, tags_any, not_tags, not_tags_any):
    response = get_modules_list(api_url, tags, tags_any, not_tags, not_tags_any)
    show_response(response)


def cli_modules_summary(api_url, tags, tags_any, not_tags, not_tags_any):
    response = get_modules_summary(api_url, tags, tags_any, not_tags, not_tags_any)
    show_response(response)


def cli_tags(api_url):
    response = get_tags(api_url)
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
