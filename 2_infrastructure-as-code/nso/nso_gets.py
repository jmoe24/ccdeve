#!usr/bin/env/python3

# this script will get info from the devices present in cisco nso

import ncs

# A good reference for Python Examples:
# https://github.com/NSO-developer/opa-example/blob/f46d16f4b40c92bc228bc8f61acac777731e88f6/packages/opa/python/opa/sub.py

def get_root():
    with ncs.maapi.single_read_trans("cisco", "python", groups=['cisco-cml']) as t:
        root = ncs.maagic.get_root(t)
        for node in root:
            print(node)

def get_device_groups():
    with ncs.maapi.single_read_trans("cisco", "python", groups=['cisco-cml']) as t:
        root = ncs.maagic.get_root(t)
        for d in root.devices.device_group:
            print(d.name)

def get_devices():
    device_list = []
    with ncs.maapi.single_read_trans("cisco", "python", groups=['cisco-cml']) as t:
        root = ncs.maagic.get_root(t)
        for d in root.devices.device:
            # print(d.name)
            device_list.append(d.name)
    return device_list

def get_config(device_name):
    with ncs.maapi.single_read_trans("cisco", "python", groups=['cisco-cml']) as t:
        root = ncs.maagic.get_root(t)

def navigate_config(device_name):
    """
    Example of how to understand and navigate a devices config in the python API.
    This example will show by printing the directory of differnet levels of the config
    """
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'cisco', 'python', groups=['cisco-cml']):
            root = ncs.maagic.get_root(m)
            device_config = root.devices.device['cat8000v-0'].config
            print(dir(device_config))
            print(dir(device_config.ip))
            print(dir(device_config.ip.dhcp))
            print(dir(device_config.ip.dhcp.snooping))

def show_commands(command, device_name):
    """
    Use a MAAPI session via maagic api to get the results of a passed show command.
    Uses the devices name in NSO as an input parameter and the commnd ie: CDP Neighbors, ip int br.
    prints the raw text results of the command.
    We do this by:
    1. Creating a NSO session
    2. Create a pointer to our device
    3. Create an input object but calling the device.live_status.ios_stats__exec.show.get_input() emthod
    4. Pass the command function input into the input objects args variable
    5. Invoke the command by passign the input object into the device.live_status.ios_stats__exec.show() method
    6. set the output variable to the result attribute of our invoked command object above
    7.Print the output
    """
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'admin', 'python'):
            root = ncs.maagic.get_root(m)
            device = root.devices.device[device_name]
            input1 = device.live_status.ios_stats__exec.show.get_input()
            input1.args = [command]
            output = device.live_status.ios_stats__exec.show(input1).result
            print(f"{device_name}:")
            print(output)

if __name__ == '__main__':
    get_root()
    # get_device_groups()
    # print(get_devices())
    # navigate_config()
    # for devices in get_devices():
    #     show_commands('ip int br', devices)
    # # device_list = get_devices()
    # for device in device_list:
    #     print(f"Device Name: {device}")