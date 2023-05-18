import typer
import settings
from info import info_impl
from modules import modules_impl
import deployments

#todo solve how to use only --version, without any command
#todo Pouzvaj log file pre debug informacie. Dhlsie chybove spravy sa nedaju citat na konzole. V pripade staci nastavit log_file = stderr. To tiez nemam urobene pre fedcloudclient.

__version__ = '0.1.0'
state = {
    'verbose': False
}

app = typer.Typer(help=f"AI4EOSC command-line client, version {__version__}", no_args_is_help=True)
app.add_typer(deployments.app, name='deployment')

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