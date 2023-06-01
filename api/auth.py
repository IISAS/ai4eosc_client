import os, settings
import liboidcagent as agent
import logging


logger = logging.getLogger(settings.logName)


class AuthorizationObject:
    """
    Abstract authorization object. Will apply authorization to a API call
    """

    def apply_authorization(self, headers: dict = None):
        ...


class BearerToken(AuthorizationObject):
    """
    Will apply a bearer token to a API call.
    """

    def __init__(self, token):
        super().__init__()
        self.token = token

    def apply_authorization(self, headers: dict = None):
        if headers:
            headers['Authorization'] = f'Bearer {self.token}'
            return headers
        else:
            headers = {'Authorization': f'Bearer {self.token}'}
            return headers

    def get_token_from_oidc_agent(oidc_agent_account, quiet=False):
        """
        Get access token from oidc-agent
        :param quiet:
        :param oidc_agent_account: account name in oidc-agent
        :return: access token, or None on error
        """

        if oidc_agent_account:
            try:
                access_token = agent.get_access_token(
                    oidc_agent_account,
                    min_valid_period=settings.MIN_ACCESS_TOKEN_TIME,
                    application_hint="fedcloudclient",
                )
                return access_token
            except agent.OidcAgentError as exception:
                logger.error(f"auth::get_tokent_from_oidc_agent: Error getting access token from oidc-agent: {exception}")
        return None


if __name__ == '__main__':
    from logsetup import start_log
    start_log()
    egi_token = os.environ.get(settings.envvar_AI4EOSC_PAPI_TOKEN)
    if (egi_token is None) or (len(egi_token) == 0):
        logger.error(f'auth: No or empty auth token, set env var {settings.envvar_AI4EOSC_PAPI_TOKEN}')
        exit(1)
    auth = BearerToken(egi_token)
    print(auth.apply_authorization())
