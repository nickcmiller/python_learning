import requests
import secrets

API_BASE_URL = 'https://otter.ai/forward/api/v1'
ENDPOINT_URL = f'{API_BASE_URL}'

print(secrets.USERNAME)


# response = requests.options(ENDPOINT_URL)
# print("RESPONSE", response)

# if response.status_code == 200:
#     allowed_methods = response.headers.get('allow')
#     print(f'Supported methods: {allowed_methods}')
# else:
#     error_message = response.json().get('error')
#     print(f'Error: {error_message}')