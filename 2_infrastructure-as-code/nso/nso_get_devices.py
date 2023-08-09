#!usr/bin/env/python3

# this script will get info from the devices present in cisco nso

import ncs

def get_devices():
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'cisco', 'cisco') as s:
            root = ncs.maagic.get_root(s)
            devices = root.devices.device
            device_list = [device.name for device in devices]
            return device_list

if __name__ == '__main__':
    device_list = get_devices()
    for device in device_list:
        print(f"Device Name: {device}")
