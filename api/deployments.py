from auth import AuthorizationObject, BearerToken
import requests
import settings

AI4EOSC_PAPI_GET_DEPLOYMENTS='{}/deployments/'


def get_deployments(api_url: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url=AI4EOSC_PAPI_GET_DEPLOYMENTS.format(api_url)
    return requests.get(url, headers=headers)


def get_deployment(api_url: str, deployment_uuid: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    return requests.get(api_url, headers=headers)


def create_deployment(api_url: str, conf: dict, auth: AuthorizationObject):
    ...


def delete_deployment(api_url: str, deployment_uuid: str, auth: AuthorizationObject):
    ...

if __name__ == '__main__':
    egi_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQVVlPaXJBM1ktZF9kR3BkajRpSkRIdzR6SGE4SVkt" \
                "YmhaZGFFajByamJVIn0.eyJleHAiOjE2ODI3MDI0ODIsImlhdCI6MTY4MjY5ODg4MiwiYXV0aF90aW1lIjoxNjgwNzEw" \
                "MjEyLCJqdGkiOiIzMWNmNzA5Ni1kYzgyLTQ3NzctODIxOS00OTUwYTlmYWMxNWIiLCJpc3MiOiJodHRwczovL2FhaS5l" \
                "Z2kuZXUvYXV0aC9yZWFsbXMvZWdpIiwic3ViIjoiMDA5ZDY4Mzc5NGI1YzJhYTdjNWQ0Yzk1ZTAwMWFmMjczYjdiOTk2" \
                "NzQ0M2RjM2I3MGY5MzE4Yjc2OWMyZjM5MUBlZ2kuZXUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0b2tlbi1wb3J0YWwi" \
                "LCJub25jZSI6ImNlMDVjZjBmMjlkZjViMWUyZTUyZTNkNTM5MjQ5NTgzIiwic2Vzc2lvbl9zdGF0ZSI6IjZiYWFkNTcy" \
                "LWJlMWQtNDZkMy04MGEwLTcwODExYzA3NmUwNiIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIGVkdXBlcnNv" \
                "bl9lbnRpdGxlbWVudCB2b3BlcnNvbl9pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiNmJhYWQ1NzItYmUxZC00NmQzLTgw" \
                "YTAtNzA4MTFjMDc2ZTA2Iiwidm9wZXJzb25faWQiOiIwMDlkNjgzNzk0YjVjMmFhN2M1ZDRjOTVlMDAxYWYyNzNiN2I5" \
                "OTY3NDQzZGMzYjcwZjkzMThiNzY5YzJmMzkxQGVnaS5ldSIsImF1dGhlbnRpY2F0aW5nX2F1dGhvcml0eSI6Imh0dHBz" \
                "Oi8vYWFpLmVnaS5ldS9nb29nbGUvc2FtbDIvaWRwL21ldGFkYXRhLnBocCJ9.YOegF5CK0jWau4_BOBfyKTiskHS1-YU" \
                "usPRbh4BLTAxUw2gqctrsaCwpXtK2VcP0dbRZSqsYMuggFsmv3yVmcx04nVUhgBjy0S4A7bz-zlBvf-vngIuFbllq1q_" \
                "axlL9H_jSuGsE1WZW37-RdXWRAx7PNz4njDLX-RuuBfkiJZU7fssKc0o9c-OYCEUjbqguzuXsdvVUfQdqn1UPMRmcouo" \
                "Cr_LVkDjS2mlhUUbThfMOv-sUQCzkoA_ttd5H7OIzXa_lV68gKZmXoPS8_rH0LzS5NdEIffSwBcijE_E6mF33OcDuyjO" \
                "ajY0C4RKwcFntzNGsIAVT2gHPrOQoEErwng"
    auth = BearerToken(egi_token)
    response = get_deployments(settings.AI4EOSC_PAPI_URL, auth)
    print(f'Status: {response.status_code}')
    print(response.text)

