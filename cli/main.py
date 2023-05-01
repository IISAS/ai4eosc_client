#todo Pouzivaj jednoduchy config subor pre default hodnot (PAPI endpoint, vo, oidc-agent konto, ..). Priority: default hodnoty v kode < default hodnoty v config subor < hodnoty parametrov nastavene v envvar < hodnoty parametrov zadane cez command-line. Neurobil som to pre fedcloudclient od zaciatku a teraz tazko upravujem.
#todo Pouzvaj log file pre debug informacie. Dhlsie chybove spravy sa nedaju citat na konzole. V pripade staci nastavit log_file = stderr. To tiez nemam urobene pre fedcloudclient.
import json

import typer
import settings
from info import info_impl
from modules import modules_impl
from deployments import deployments_impl

#todo solve how to use only --version, without any command

__version__ = '0.1.0'
state = {
    'verbose': False
}

app = typer.Typer(help=f"AI4EOSC command-line client, version {__version__}", no_args_is_help=True)

@app.command()
def info(
        object: str = typer.Argument(
            None,
            help='module name for its default config, v=<number> for info about API version, or nothing for info about the platform'),
        api_url: str = typer.Option(
            settings.AI4EOSC_PAPI_URL,
            help="AI4EOSC PAPI URL",
            envvar='AI4EOSC_PAPI_URL'),
        auth_token: str = typer.Option(
            None,
            '--auth-token', '-t',
            help='authorization bearer token',
            envvar='AI4EOSC_PAPI_TOKEN')
        ):
    return info_impl(object, api_url, auth_token)


@app.command()
def modules(
        module_name: str = typer.Argument(
            None,
            help='module name to query or update; leave out for list of modules or their summary'),
        api_url: str = typer.Option(
            settings.AI4EOSC_PAPI_URL,
            help="AI4EOSC PAPI URL",
            envvar='AI4EOSC_PAPI_URL'),
        auth_token: str = typer.Option(
            None,
            '--auth-token', '-t',
            help='authorization bearer token',
            envvar='AI4EOSC_PAPI_TOKEN'),
        summary: bool = typer.Option(
            False,
            '--summary', '-s',
            help='Provide summary of modules instead of their listing'),
        update: bool = typer.Option(
            False,
            '--update', '-u',
            help='Update metadata instead of querying it'),
        new_metadata: str = typer.Option(
            None,
            '--new-metadata', '-nm',
            help='name of JSON file with new metadata, if updating module')
        ):
    return modules_impl(module_name, api_url, auth_token, summary, update, new_metadata)

@app.command()
def deployments(
        deployment_uuid: str = typer.Argument(
            None,
            help='deployment UUID'),
        api_url: str = typer.Option(
            settings.AI4EOSC_PAPI_URL,
            help="AI4EOSC PAPI URL",
            envvar='AI4EOSC_PAPI_URL'),
        auth_token: str = typer.Option(
            None,
            '--auth-token', '-t',
            help='authorization bearer token',
            envvar='AI4EOSC_PAPI_TOKEN'),
        create: bool = typer.Option(
            False,
            '--create', '-c',
            help='create a deployment using provided JSON file'),
        delete: bool = typer.Option(
            False,
            '--delete', '-d',
            help='delete the named deployment'),
        new_deployment: str = typer.Option(
            None,
            '--new-deployment', '-nd',
            help='name of JSON file with new deployment specification')
        ):
    return deployments_impl(deployment_uuid, api_url, auth_token, create, delete, new_deployment)

@app.callback()
def main(
        version: bool = typer.Option(None, "--version", "-v", help='display version and exit', is_eager=True),
        verbose: bool = False):
    """
    Manage users in the awesome CLI app.
    """
    if version:
        print(__version__)
        raise typer.Exit()

    if verbose:
        print("Will write verbose output")
        state['verbose'] = True


if __name__ == "__main__":
    app()