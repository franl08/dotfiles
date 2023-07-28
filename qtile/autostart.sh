#!/usr/bin/bash

lxsession &
nm-applet &
blueberry-tray &
~/.fehbg &
picom -b &
flameshot &
/usr/bin/emacs --daemon &
export _JAVA_AWT_WM_NONREPARENTING=1 &
/home/tgvp/.scripts/autoupdate.py
