|                                  |                                                                                                                  |
|----------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![](EN-Funded by the EU-POS.jpg) | This work is funded by European Union through the AI4EOSC project (Horizon Europe) under Grant number 101058593. |

[![GitHub Super-Linter](https://github.com/IISAS/ai4eosc_client/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/marketplace/actions/super-linter)
[![Tox](https://github.com/IISAS/ai4eosc_client/actions/workflows/tox.yml/badge.svg?branch=main)](https://tox.wiki/en/latest/)

<div align="center">
  <img src="https://ai4eosc.eu/wp-content/uploads/sites/10/2022/09/horizontal-transparent.png" alt="logo" width="500"/>
</div>

# AI4OS Command-line client - ai4os-client
This command-line interface (CLI) provides access to the functions of the [AI4OS platform API (PAPI)](https://github.com/AI4EOSC/ai4-papi#readme).

## Basic Usage
The CLI mimics the logical division of functions of the AI4OS PAPI into three main groups (commands):
- info - provides information about the default deployment, the platform or API version.
- deployment - allows to work with deployments.
- module - allows to work with modules.

Each of these commands then requires one of several sub-commands, which are described below.

## Common Options and Arguments
The CLI's functioning is controlled by options and arguments, some of which can be used with several commands and sub-commands.
Here are the most important ones. A complete list of options and arguments can be obtained using the <em>--help</em> option.
- --help - displays context help, depending on the used command and sub-command. Lists all available options and arguments and their meaning.

For module filtering by tags, these options can be used:
- --tags - only modules tagged by all the specified tags will be included.
- --tags-any - modules that contain at least some of the specified tags will be included.
- --not-tags - modules that do not contain any of the specified tags will be included.
- --not-tags-any - modules that do not contain at least some of the specified tags will be included.

## Authentication
Authentication in the PAPI is done using OICD tokens. A token need to be provided to the CLI, which will then forward
them to the PAPI. The token can be provided in three different ways:
- by providing it directly using the --auth-token or -t option
- by taking it from the oicd-agent by providing its account name with the --oidc-agent-account option
- by using a mytoken server, providing its URL with --mytoken-server and token name with --mytoken options.

## "info" command
Provides basic information:
- api-info - print API information.
- default-deployment - print default deployment information.
- platform-info - print platform information.

## "deployment" command
Provides interface for work with deployments:
- create - create a new deployment.
- delete - delete an existing deployment.
- list - list existing deployments.
- show - show information about a deployment, identified by its UUID.

## "module" commnad
Provides interface for work with modules:
- list-modules - list existing modules, with filtering by tags.
- modules-summary - print summary of all existing modules, with optional...
- show-module - print module information.
- tags - print all existing tags.
- update-module - update module metadata.


