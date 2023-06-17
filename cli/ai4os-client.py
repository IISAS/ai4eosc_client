import typer
import info, modules, deployments, settings
import logging
from logsetup import start_log


logger = logging.getLogger(settings.logName)

# todo solve how to use only --version, without any command

__version__ = "0.3.0"
state = {"verbose": False}

app = typer.Typer(name="ai4os_client", help=f"AI4OS command-line client, version {__version__}", no_args_is_help=True)
app.add_typer(deployments.app, name='deployment')
app.add_typer(info.app, name='info')
app.add_typer(modules.app, name='module')


@app.callback()
def main(version: bool = typer.Option(None, "--version", "-v", help='display version and exit', is_eager=True), verbose: bool = False):
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
    start_log()
    app()
