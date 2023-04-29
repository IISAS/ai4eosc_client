import json
import settings
from api.info import get_platform_info, get_api_version_info, get_default_deployment_conf
from api.auth import BearerToken


def deployments_impl(deplyment, auth_token):
    ...
