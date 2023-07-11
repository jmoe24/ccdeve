#!/bin/bash
# Authored by Josh Morris
# Create CSR and KEY for Digicert wildcard using conf file

# set date variables
date=$(date "+%m-%d-%y")
year=$(date +%Y)
nextyear=$((year + 1))

# config file for cert values
config_file=csr_conf.cnf

# get URL/application name from user input
read -p "Enter the URL/Application name for CSR & KEY using underscores (Ex: isenew_stjude_org): " name
#echo "URL Name:: ${name}"

# use openSSL to create CSR and KEY using variables from above
openssl req -newkey rsa:4096 -nodes -keyout wildcard_$nextyear/$name.key -out wildcard_$nextyear/$name.csr -config $config_file
