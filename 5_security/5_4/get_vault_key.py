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
SECRET_NAME = 'test1'
SECRET_PATH = f'/v1/cubbyhole/{SECRET_NAME}'

# Path to your client certificate and private key files
# Note: This path is hardcoded for the CWS
CA_CERT_PATH = '/home/expert/gitrepo/4_containers/docker/vault_docker-compose/config/certs/vault_ca_certificate.crt'
CLIENT_CERT_PATH = '/home/expert/gitrepo/4_containers/docker/vault_docker-compose/config/certs/vault_certificate.crt'
CLIENT_KEY_PATH = '/home/expert/gitrepo/4_containers/docker/vault_docker-compose/config/certs/vault_privatekey.key'

# Make the API request to Vault
HEADERS = {'X-Vault-Token': VAULT_TOKEN}
response = requests.get(
    f'{VAULT_URL}{SECRET_PATH}',
    headers=HEADERS,
    cert=(CLIENT_CERT_PATH, CLIENT_KEY_PATH),  # Provide client certificate and key
    verify=CA_CERT_PATH
)

# Check if the request was successful (status code 200)

if response.status_code == 200:
    # Extract the secret data from the response
    secret_data = response.json().get('data', {})
    retrieved_password = secret_data.get(SECRET_NAME, 'default_value')

    # Print the retrieved secret value
    print(f"Retrieved 'key_name' from the '{SECRET_NAME}' secret: {retrieved_password}")

    # Now 'retrieved_password' holds the secret value retrieved from Vault
else:
    print(f"Failed to retrieve secret. Status code: {response.status_code}")
