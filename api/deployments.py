from auth import AuthorizationObject, BearerToken
import requests
import settings

AI4EOSC_PAPI_GET_DEPLOYMENTS='{}/v1/deployments/'
AI4EOSC_PAPI_CREATE_DEPLOYMENT='{}/v1/deployments/'
AI4EOSC_PAPI_GET_DEPLOYMENT='{}/v1/deployments/{}'
AI4EOSC_PAPI_DELETE_DEPLOYMENT='{}/v1/deployments/{}'


def get_deployments(api_url: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_GET_DEPLOYMENTS.format(api_url)
    return requests.get(url, headers=headers)


def get_deployment(api_url: str, deployment_uuid: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_GET_DEPLOYMENT.format(api_url, deployment_uuid)
    return requests.get(url, headers=headers)


def create_deployment(api_url: str, conf: dict, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_CREATE_DEPLOYMENT.format(api_url)
    return requests.post(url, headers=headers, json=conf)


def delete_deployment(api_url: str, deployment_uuid: str, auth: AuthorizationObject):
    headers = auth.apply_authorization()
    url = AI4EOSC_PAPI_DELETE_DEPLOYMENT.format(api_url, deployment_uuid)
    return requests.delete(url, headers=headers)


if __name__ == '__main__':
    egi_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQVVlPaXJBM1ktZF9kR3BkajRpSkRIdzR6SGE4SVktYmhaZGFFajByamJVIn0.eyJleHAiOjE2ODI3NTk2NDgsImlhdCI6MTY4Mjc1NjA0OCwiYXV0aF90aW1lIjoxNjgwNzEwMjEyLCJqdGkiOiI4YzgwZWE3Zi04OGU4LTQwZmQtYTAyZS01NTU5NmI0ZTdmNDciLCJpc3MiOiJodHRwczovL2FhaS5lZ2kuZXUvYXV0aC9yZWFsbXMvZWdpIiwic3ViIjoiMDA5ZDY4Mzc5NGI1YzJhYTdjNWQ0Yzk1ZTAwMWFmMjczYjdiOTk2NzQ0M2RjM2I3MGY5MzE4Yjc2OWMyZjM5MUBlZ2kuZXUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0b2tlbi1wb3J0YWwiLCJub25jZSI6ImNlMDVjZjBmMjlkZjViMWUyZTUyZTNkNTM5MjQ5NTgzIiwic2Vzc2lvbl9zdGF0ZSI6IjZiYWFkNTcyLWJlMWQtNDZkMy04MGEwLTcwODExYzA3NmUwNiIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIGVkdXBlcnNvbl9lbnRpdGxlbWVudCB2b3BlcnNvbl9pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiNmJhYWQ1NzItYmUxZC00NmQzLTgwYTAtNzA4MTFjMDc2ZTA2Iiwidm9wZXJzb25faWQiOiIwMDlkNjgzNzk0YjVjMmFhN2M1ZDRjOTVlMDAxYWYyNzNiN2I5OTY3NDQzZGMzYjcwZjkzMThiNzY5YzJmMzkxQGVnaS5ldSIsImF1dGhlbnRpY2F0aW5nX2F1dGhvcml0eSI6Imh0dHBzOi8vYWFpLmVnaS5ldS9nb29nbGUvc2FtbDIvaWRwL21ldGFkYXRhLnBocCJ9.WqTx8Qy3IJLLwWsmctbc9JA9Yq8p2i-DA3WWSyVHAOfUONou5-zSc0RsU2LhZ83zGu6S0gOcMNeeszbVUl_K3zxwkpmzJUYLT-YrZP1VGfaXfuR_Vz4u46EWkBa93L7S0LpTjY7OefUFsrB6Qz5SvWLSD74SeVLmcYbyZ5pxIob8j8nBqY-z7zpZMmZvBZnVSzS7LHGk-kq8lAShZlIWGPY7RzPwmUDMNfcnVYa7wWC4oZLDGa3Bia85N-sdnBhQgc_74W4lsqQLwFQwNw32xBS4iCbjfFhDZMg_4MWwwhJA_9SHgjhHjN6fi40aesKbv1K1sgkD4eWlasLiI1QIjA"
    auth = BearerToken(egi_token)
    response = get_deployments(settings.AI4EOSC_PAPI_V1_URL, auth)
    print(f'Status: {response.status_code}')
    print(response.text)

