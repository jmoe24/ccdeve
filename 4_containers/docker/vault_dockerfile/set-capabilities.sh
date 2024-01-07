#!/bin/sh
#set -e

# Add IPC_LOCK capability to the Vault binary
setcap cap_ipc_lock=+ep /usr/sbin/vault

