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
    auth = BearerToken('###bearertoken###')
    print(auth.apply_authorization())