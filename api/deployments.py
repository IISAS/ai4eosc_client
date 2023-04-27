from auth import AuthorizationObject


def get_deployments(auth: AuthorizationObject):
    ...


def get_deployment(deployment_uuid: str, auth: AuthorizationObject):
    ...


def create_deployment(conf: dict, auth: AuthorizationObject):
    ...


def delete_deployment(deployment_uuid: str, auth: AuthorizationObject):
    ...
