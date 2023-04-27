class AuthorizationObject:
    '''
    Abstract authorization object. Will apply authorization to a API call
    '''
    def apply_authorization(self):
        ...

class BearerToken(AuthorizationObject):
    '''
    Will apply a bearer token to a API call.
    '''
    def apply_authorization(self):
        ...
