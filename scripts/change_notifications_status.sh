#!/usr/bin/bash

is_paused=$(dunstctl is-paused)

if $is_paused;
then
dunstctl set-paused false
else
dunstctl set-paused true
fi
