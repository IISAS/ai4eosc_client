import typer
import info, modules, deployments

# todo solve how to use only --version, without any command
# todo Pouzvaj log file pre debug informacie. Dhlsie chybove spravy sa nedaju citat na konzole. V pripade staci nastavit log_file=stderr. To tiez nemam urobene pre fedcloudclient.

__version__ = "0.3.0"
state = {"verbose": False}

app = typer.Typer(help=f"AI4EOSC command-line client, version {__version__}", no_args_is_help=True)
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
    app()
