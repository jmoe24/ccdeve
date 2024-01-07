#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Author: Josh Morris
Description: Get secret from Vault Server
'''

import requests

# Replace with your Vault server URL and token
VAULT_URL = 'https://vault.joshlab.com:8200'
VAULT_TOKEN = 'hvs.lqL7JialYYuk7AVcCbHSr2cP'

# Vault API endpoint to retrieve the secret
SECRET_PATH = '/v1/cubbyhole/test'

# Make the API request to Vault
HEADERS = {'X-Vault-Token': VAULT_TOKEN}
RESPONSE = requests.get(f'{VAULT_URL}{SECRET_PATH}', headers=HEADERS)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the secret data from the response
    secret_data = response.json().get('data', {})
    josh_test = secret_data.get('test', 'default_value')  # Replace 'key_name' with your specific field name

    # Print the retrieved secret value
    print(f"Retrieved 'key_name' from the 'test' secret: {josh_test}")

    # Now 'josh_test' holds the secret value retrieved from Vault
else:
    print(f"Failed to retrieve secret. Status code: {response.status_code}")

