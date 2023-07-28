#!/usr/bin/python3

from datetime import datetime
import subprocess
import sys

f = open('/home/tgvp/.scripts/.lastupdate', 'r')
last_update = datetime.strptime(f.read(), f"%Y-%m-%d")
f.close()
days_between = (datetime.now() - last_update).days

updated = False

if days_between >= 7 or len(sys.argv) > 1:
    process = subprocess.call('alacritty -e sudo pacman -Syuu', shell=True)
    updated = True

if updated:
    f = open('/home/tgvp/.scripts/.lastupdate', 'w')
    f.write(datetime.strftime(datetime.now(), f"%Y-%m-%d"))
