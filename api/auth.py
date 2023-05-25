import os, settings
class AuthorizationObject:
    '''
    Abstract authorization object. Will apply authorization to a API call
    '''
    def apply_authorization(self, headers: dict = None):
        ...

class BearerToken(AuthorizationObject):
    '''
    Will apply a bearer token to a API call.
    '''

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


if __name__ == '__main__':
    egi_token = os.environ.get(settings.envvar_AI4EOSC_PAPI_TOKEN)
    if (egi_token is None) or (len(egi_token) == 0):
        print(f'No or empty auth token, set env var {settings.envvar_AI4EOSC_PAPI_TOKEN}')
        exit(1)
    auth = BearerToken(egi_token)
    print(auth.apply_authorization())