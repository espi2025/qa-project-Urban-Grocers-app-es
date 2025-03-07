import requests
import configuration
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def create_kit(kit_body,auth_thoken):
    headers = data.headers.copy()
    headers['Authorization'] = f'Bearer {auth_thoken}'
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json= kit_body,
                        headers = headers
                        )

print('post new user')
new_user = post_new_user(data.user_body)
new_user_token =new_user.json()['authToken']
print(new_user_token)

print(data.headers)
print('post kit for user')
new_kit =post_new_user(data.kit_body.copy())
print(new_kit.json())








