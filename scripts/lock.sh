#!/bin/sh

BLANK='#00000000'
CLEAR='#ffffff22'
DEFAULT='#b4f9f8'
TEXT='#bb9af7'
WRONG='#f7768e'
VERIFYING='#73daca'

i3lock \
--insidever-color=$CLEAR     \
--ringver-color=$VERIFYING   \
\
--insidewrong-color=$CLEAR   \
--ringwrong-color=$WRONG     \
\
--inside-color=$BLANK        \
--ring-color=$DEFAULT        \
--line-color=$BLANK          \
--separator-color=$DEFAULT   \
\
--verif-color=$TEXT          \
--wrong-color=$TEXT          \
--time-color=$TEXT           \
--date-color=$TEXT           \
--layout-color=$TEXT         \
--keyhl-color=$WRONG         \
--bshl-color=$WRONG          \
\
--screen 1                   \
--blur 10                    \
--clock                      \
--indicator                  \
--time-str="%H:%M:%S"        \
--date-str="%d-%m-%Y"        \
