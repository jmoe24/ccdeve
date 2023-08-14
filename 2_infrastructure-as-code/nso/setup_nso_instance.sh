#! /bin/bash

# Author: Josh Morris
# This script is meant to handle all the initial setup of NSO (after it has been installed)
# After this script, you should be able to get working with reading and writing via NSO
# This script assumes NSO has been installed and the ncsrc script has been run, which adds ncs to PATH
# Be sure to source this file instead of just execute so the job runs in the current shell (source setup_nso_instance.sh)
# Pass in the following arguments
# $1: Name of the instance (Ex: ./setup_nso_instance test-instance)
# $2: Name of the template package (Ex: ./setup_nso_instance test-instance ios_routers_package)


# Create NSO instance. An instance here is like a Python virtual environment. You can only run one instance at a time
# Instance uses the Cisco IOS CLI NED
# Run this script in the directory where you ultimately want your output \
# In my case, I want my jobs to live in my github repositories, NOT the NSO directory

cd /home/expert/gitrepo/2_infrastructure-as-code/nso
ncs-setup --package ~/nso/nso6.1/packages/neds/cisco-ios-cli-6.92 --dest $1
printf "NSO Instance '$1' created in: $PWD/$1\n"


# Create NCS package using the python-and-temlpate type
cd $1/packages
ncs-make-package --service-skeleton python-and-template $2

# Change into new directory and start ncs
cd ..
printf "$PWD\n"
printf "Starting NCS\n"
ncs
printf "NCS Started\n"

# Print ncs status to ensure service is started
ncs --status | grep status

# After this, configure the authgroup and devices. Then sync-from devices and start other development
ncs_cli -C -u admin
!
!
config
load merge ../nso-configs/nso-inventory.cfg

# !
# config
# devices authgroups group cisco-cml default-map remote-name cisco remote-password cisco remote-secondary-password cisco
# !
# devices device cat8000v-0 address 192.168.86.251 port 22 device-type cli ned-id cisco-ios-cli-6.92
# authgroup cisco-cml
# state admin-state unlocked
# device-type cli protocol ssh
# ssh host-key-verification none
# devices device cat8000v-1 address 192.168.86.252 port 22 device-type cli ned-id cisco-ios-cli-6.92
# authgroup cisco-cml
# state admin-state unlocked
# device-type cli protocol ssh
# ssh host-key-verification none
# devices device cat8000v-2 address 192.168.86.253 port 22 device-type cli ned-id cisco-ios-cli-6.92
# authgroup cisco-cml
# state admin-state unlocked
# device-type cli protocol ssh
# ssh host-key-verification none
# exit
# devices device-group cisco-cml
# device-name cat8000v-0
# device-name cat8000v-1
# device-name cat8000v-2
# exit
# commit
# exit