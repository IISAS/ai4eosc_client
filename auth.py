import logging
import settings
import liboidcagent as agent
import requests

logger = logging.getLogger(settings.logName)


def get_token_from_oidc_agent(oidc_agent_account):
    """
    Get access token from oidc-agent
    :param oidc_agent_account: account name in oidc-agent
    :return: access token, or None on error
    """

    if oidc_agent_account:
        try:
            access_token = agent.get_access_token(oidc_agent_account, min_valid_period=settings.MIN_ACCESS_TOKEN_TIME, application_hint=settings.application_hint)
            return access_token
        except agent.OidcAgentError as exception:
            logger.error(f'oidc_agent_account: Error getting access token from oidc-agent: {exception}')
    return None


def get_token_from_mytoken_server(mytoken, mytoken_server=settings.mytoken_default_server):
    """
    Get access token from mytoken server
    :param mytoken: mytoken id string
    :param mytoken_server: mytoken server URL
    :return: access token, or None on error
    """

    if mytoken and mytoken_server:
        try:
            data = {
                "grant_type": "mytoken",
                "mytoken": mytoken,
            }
            req = requests.post(
                mytoken_server + "/api/v0/token/access",
                json=data,
            )
            req.raise_for_status()
            return req.json().get("access_token")
        except requests.exceptions.HTTPError as exception:
            logger.error(f'get_token_from_mytoken_server: cannot get token from mytoken: {exception}')
    return None


def get_access_token(
    oidc_agent_account,
    mytoken,
    mytoken_server,
):
    """
    Get access token: obtains access token from oidc-agent or mytoken

    Check expiration time of access token
    Log error if no valid token exists

    :param oidc_agent_account: name of the oidc-agent account to use
    :param mytoken: mytoken id string
    :param mytoken_server: mytoken server URL
    :return: access token
    """

    try:
        access_token = None

        if mytoken:
            access_token = get_token_from_mytoken_server(mytoken, mytoken_server)

        if oidc_agent_account and access_token is None:
            access_token = get_token_from_oidc_agent(oidc_agent_account)

        if access_token is None:
            logger.warning('get_access_token: could not get any access token from mytoken or oidc-agent')

        return access_token
    except Exception as e:
        logger.error(f'get_access_token: exception: {str(e)}')
        return None
