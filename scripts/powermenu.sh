#!/bin/bash

options="Cancel\nReboot\nLock\nShutdown"
selected=$(echo -e $options | dmenu)
if [[ $selected = "Shutdown" ]]; then
	poweroff
elif [[ $selected = "Reboot" ]]; then
	reboot
elif [[ $selected = "Lock" ]]; then
	bash /home/tgvp/.scripts/lock.sh
elif [[ $selected = "Cancel" ]]; then
	return
fi
