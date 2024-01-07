#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Author: Josh Morris
Description: Get secret from Vault Server using class based Connection Handler
'''

import requests

class VaultClient:
    def __init__(self, url, token, ca_cert_path, client_cert_path, client_key_path):
        self.url = url
        self.token = token
        self.ca_cert_path = ca_cert_path
        self.client_cert_path = client_cert_path
        self.client_key_path = client_key_path
        self.session = self._create_session()

    def _create_session(self):
        session = requests.Session()
        session.cert = (self.client_cert_path, self.client_key_path)
        session.verify = self.ca_cert_path
        return session

    def get_secret(self, secret_name):
        secret_path = f'/v1/cubbyhole/{secret_name}'
        headers = {'X-Vault-Token': self.token}

        response = self.session.get(f'{self.url}{secret_path}', headers=headers)
        
        if response.status_code == 200:
            secret_data = response.json().get('data', {})
            retrieved_password = secret_data.get(secret_name, 'default_value')
            print(f"Retrieved '{secret_name}' from the secret: {retrieved_password}")
            return retrieved_password
        else:
            print(f"Failed to retrieve secret. Status code: {response.status_code}")
            return None

# Usage example
VAULT_URL = 'https://vault.joshlab.com:8200'
VAULT_TOKEN = 'hvs.lqL7JialYYuk7AVcCbHSr2cP'
CA_CERT_PATH = '/home/expert/gitrepo/4_containers/docker/vault_docker-compose/config/certs/vault_ca_certificate.crt'
CLIENT_CERT_PATH = '/home/expert/gitrepo/4_containers/docker/vault_docker-compose/config/certs/vault_certificate.crt'
CLIENT_KEY_PATH = '/home/expert/gitrepo/4_containers/docker/vault_docker-compose/config/certs/vault_privatekey.key'

# Create a VaultClient instance
vault_client = VaultClient(VAULT_URL, VAULT_TOKEN, CA_CERT_PATH, CLIENT_CERT_PATH, CLIENT_KEY_PATH)

# Get the secret
retrieved_secret = vault_client.get_secret('test1')