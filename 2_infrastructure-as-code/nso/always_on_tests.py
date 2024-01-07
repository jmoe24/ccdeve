#! /usr/bin/python3

"""
Script to get all devices from the always-on Cisco NSO Sandbox
Address: sandbox-nso-1.cisco.com
Username: developer
Password: Services4Ever
"""

import json
import requests

NSO_BASE_URL = 'https://sandbox-nso-1.cisco.com/restconf/data'
NSO_USERNAME = 'developer'
NSO_PASSWORD = 'Services4Ever'

BASIC_AUTH =  (NSO_USERNAME, NSO_PASSWORD)

SAMPLE_IOS_DEVICE = 'dist-rtr01'

# For HTTP GET, we need to accept a variety of YANG data encoded as JSON.
# This technique joins all the list elements together with a comma to
# create a single, comma-delineated string value for the Accept header.
ACCEPT_LIST = [
        "application/vnd.yang.api+json",
        "application/vnd.yang.datastore+json",
        "application/vnd.yang.data+json",
        "application/vnd.yang.collection+json",
    ]

GET_HEADERS = {"Accept": ",".join(ACCEPT_LIST)}

def GET_RESTCONF_DATA():
    response = requests.get(f"{NSO_BASE_URL}",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

def GET_DEVICE_CONFIG():
    response = requests.get(f"{NSO_BASE_URL}/tailf-ncs:devices/device={SAMPLE_IOS_DEVICE}",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

def GET_DEVICE_PLATFORM():
    response = requests.get(f"{NSO_BASE_URL}/tailf-ncs:devices/device={SAMPLE_IOS_DEVICE}/platform",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)        
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

def GET_SHOW_INTERFACES():
    response = requests.get(f"{NSO_BASE_URL}/tailf-ncs:devices/device={SAMPLE_IOS_DEVICE}/config/tailf-ned-cisco-ios:interface/",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

def GET_SPECIFIC_INTERFACE():
    response = requests.get(f"{NSO_BASE_URL}/tailf-ncs:devices/device={SAMPLE_IOS_DEVICE}/config/tailf-ned-cisco-ios:interface/GigabitEthernet=4",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

def GET_DEVICE_GROUPS():
    response = requests.get(f"{NSO_BASE_URL}/tailf-ncs:devices/device-group",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

def GET_SPECIFIC_DEVICE_GROUPS():
    response = requests.get(f"{NSO_BASE_URL}/tailf-ncs:devices/device-group=IOS-DEVICES",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

def VIEW_DEVICE_STATUS():
    response = requests.get(f"{NSO_BASE_URL}/tailf-ncs:devices/device={SAMPLE_IOS_DEVICE}/live-status",
        auth=BASIC_AUTH,
        headers=GET_HEADERS,
        verify=False,)
    print(json.dumps(response.json(), indent=4))
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

if __name__ == '__main__':
    # GET_RESTCONF_DATA()
    # GET_DEVICE_CONFIG()
    # GET_DEVICE_PLATFORM()
    # GET_SHOW_INTERFACES()
    # GET_SPECIFIC_INTERFACE()
    # GET_DEVICE_GROUPS()
    # GET_SPECIFIC_DEVICE_GROUPS()
    # VIEW_DEVICE_STATUS()