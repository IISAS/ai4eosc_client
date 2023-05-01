from api.auth import BearerToken, AuthorizationObject
import settings
import requests

AI4EOSC_PAPI_GET_DEFAULT_DEPLOYMENT_CONF='{}/v1/info/conf/{}'
AI4EOSC_PAPI_GET_PLATFORM_INFO='{}'
AI4EOSC_PAPI_GET_API_VERSION_INFO='{}/{}'

def get_default_deployment_conf(api_url: str, module_name: str, auth: AuthorizationObject):
    url=AI4EOSC_PAPI_GET_DEFAULT_DEPLOYMENT_CONF.format(api_url, module_name)
    headers = auth.apply_authorization()
    return requests.get(url, headers=headers)


def get_platform_info(api_url: str):
    url=AI4EOSC_PAPI_GET_PLATFORM_INFO.format(api_url)
    return requests.get(url)


def get_api_version_info(api_url: str, version: str):
    url=AI4EOSC_PAPI_GET_API_VERSION_INFO.format(api_url, version)
    return requests.get(url)


if __name__ == '__main__':
    #egi_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQVVlPaXJBM1ktZF9kR3BkajRpSkRIdzR6SGE4SVktYmhaZGFFajByamJVIn0.eyJleHAiOjE2ODI3NTY2NDIsImlhdCI6MTY4Mjc1MzA0MiwiYXV0aF90aW1lIjoxNjgwNzEwMjEyLCJqdGkiOiI3MWEwODIwZi02OTRiLTRlNmQtYWE2ZS00MmVhY2M1Y2I0ODQiLCJpc3MiOiJodHRwczovL2FhaS5lZ2kuZXUvYXV0aC9yZWFsbXMvZWdpIiwic3ViIjoiMDA5ZDY4Mzc5NGI1YzJhYTdjNWQ0Yzk1ZTAwMWFmMjczYjdiOTk2NzQ0M2RjM2I3MGY5MzE4Yjc2OWMyZjM5MUBlZ2kuZXUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0b2tlbi1wb3J0YWwiLCJub25jZSI6ImNlMDVjZjBmMjlkZjViMWUyZTUyZTNkNTM5MjQ5NTgzIiwic2Vzc2lvbl9zdGF0ZSI6IjZiYWFkNTcyLWJlMWQtNDZkMy04MGEwLTcwODExYzA3NmUwNiIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIGVkdXBlcnNvbl9lbnRpdGxlbWVudCB2b3BlcnNvbl9pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiNmJhYWQ1NzItYmUxZC00NmQzLTgwYTAtNzA4MTFjMDc2ZTA2Iiwidm9wZXJzb25faWQiOiIwMDlkNjgzNzk0YjVjMmFhN2M1ZDRjOTVlMDAxYWYyNzNiN2I5OTY3NDQzZGMzYjcwZjkzMThiNzY5YzJmMzkxQGVnaS5ldSIsImF1dGhlbnRpY2F0aW5nX2F1dGhvcml0eSI6Imh0dHBzOi8vYWFpLmVnaS5ldS9nb29nbGUvc2FtbDIvaWRwL21ldGFkYXRhLnBocCJ9.hvKBkbIUiJdzH0JJxSJLQ3fuUYhZ3dFhXKyKNIxRYc0LgIx2SHDCUUPBlFmUggGcQJsSNWyLR7UKOdxyigtlYPgEXsmeLKQJ0m4pHaqgMbBTQCY4iYq_k-Uy2-BNHl9KjkxUErG9SXxBk_Wns4jCnhqOiPGG839sEs8lVKFvy2FHH_gj_rhrzinXBK-fa4vD9xh7ckUachkqfuLBomM8lJBq8dwOyMWJ77uMEx6EFdiqYSRQCKrpztXYK1wXVd0Q8I13jKaryMtcFrHPCy9KSM_04lrtG2EHZb2AfouLn7s8QS4h731IP_vWwacJZIksmlTI2MxvBHVZI95xCRyl0w"
    #auth = BearerToken(egi_token)
    #response = get_default_deployment_conf(settings.AI4EOSC_PAPI_V1_URL, 'DEEP-OC-dogs_breed_det', auth)
    #print(f'Status: {response.status_code}')
    #print(response.text)
    response = get_platform_info(settings.AI4EOSC_PAPI_URL)
    print(f'Status: {response.status_code}')
    print(response.text)
    response = get_api_version_info(settings.AI4EOSC_PAPI_URL, 'v1')
    print(f'Status: {response.status_code}')
    print(response.text)



