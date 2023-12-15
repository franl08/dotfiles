# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -*- coding: utf-8 -*-
from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess
from spotify import Spotify
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401


mod = "mod4"
terminal = "alacritty"
browser = "firefox"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "KP_Add", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "KP_Subtract", lazy.layout.shrink(), desc="Grow window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod, "shift"],
        "a",
        lazy.spawn("/home/tgvp/.config/dmenu/dmenu_run_history"),
        desc="Launch dmenu_run",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("/home/tgvp/.scripts/powermenu.sh"),
        desc="Shows dmenu power menu",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("discord"), desc="Spawn Discord"),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn("flameshot gui"),
        desc="Take screenshot with Flameshot",
    ),
    Key([mod], "s", lazy.spawn("spotify"), desc="Spawn Spotify"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Spawn Firefox"),
    Key([mod], "f", lazy.spawn("thunar"), desc="Spawn Thunar"),
    Key([mod, "shift"], "z", lazy.spawn("zathura"), desc="Spawn Zathura"),
    Key([mod], "z", lazy.spawn("zotero"), desc="Spawn Zotero"),
    Key([mod], "o", lazy.spawn("obsidian"), desc="Spawn Obsidian"),
    Key([mod, "shift"], "r", lazy.spawn(
        "alacritty -e ranger"), desc="Spawn Ranger"),
    Key(
        [mod, "shift"], "e", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Spawn emacs"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.spawn("/home/tgvp/.scripts/lock.sh"),
        desc="Lock Screen",
    ),
    Key(
        [mod, "shift"],
        "u",
        lazy.spawn("/home/tgvp/.scripts/autoupdate.py"),
        desc="Updates system",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.spawn("/home/tgvp/.scripts/home.sh"),
        desc="Home screens layout",
    ),
    Key(
        [mod, "shift"],
        "i",
        lazy.spawn("/home/tgvp/.scripts/inesc.sh"),
        desc="Inesctec screens layout",
    ),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn("/home/tgvp/.scripts/change_wallpaper.sh"),
        desc="Change Wallpaper",
    ),
    Key(
        [mod, "shift"],
        "g",
        lazy.spawn("~/.scripts/copilot.sh"),
        desc="Copy copilot token",
    ),
    Key(
        [mod, "shift"],
        "m",
        lazy.spawn(
            "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"
        ),
        desc="Pause/Play music on spotify",
    ),
    Key(
        [mod, "shift"],
        "n",
        lazy.spawn(
            "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous"
        ),
        desc="Previous music on Spotify",
    ),
    Key(
        [mod, "shift"],
        "comma",
        lazy.spawn(
            "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"
        ),
        desc="Next music on Spotify",
    ),
    Key(
        [mod, "control"],
        "s",
        lazy.spawn("/home/tgvp/.scripts/change_notifications_status.sh"),
        desc="Snooze/Activate notifications.",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "period", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("/home/tgvp/.scripts/bright +"),
        desc="Increase screen brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("/home/tgvp/.scripts/bright -"),
        desc="Decrease screen brightness",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl -- set-sink-volume 0 +5%"),
        desc="Increase volume by 5%",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl -- set-sink-volume 0 -5%"),
        desc="Decrease volume by 5%",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute 0 toggle"),
        desc="(De)mute volume",
    ),
    Key(
        [],
        "XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute 1 toggle"),
        desc="(De)mutes microphone",
    ),
    Key(["shift"], "F9", lazy.spawn("arandr"),
        "Opens arandr to screens configuration"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# groups = [Group(i) for i in "123456789"]

groups = [
    Group("dev", layout="monadtall"),
    Group("www", layout="max"),
    Group("chat", layout="monadtall"),
    Group("mus", layout="monadtall"),
    Group("obs", layout="max"),
    Group("shu", layout="monadtall"),
    Group("fun", layout="max"),
]

for i, group in enumerate(groups, 1):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(i),
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


dgroups_key_binder = simple_key_binder("mod4")


layout_theme = {
    "border_width": 1,
    "margin": 1,
    "border_focus": "#A2EEE2",
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Columns(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="UbuntuMono", fontsize=12, padding=3, background=["#1c1f24", "#1c1f24"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(linewidth=0, padding=4),
                widget.GroupBox(
                    active="ffffff",
                    highlight_method="line",
                    this_screen_border="#A2EEE2",
                    other_screen_border="#808080",
                    this_current_screen_border="#A2EEE2",
                    borderwidth=1,
                ),
                widget.Spacer(),
                Spotify(foreground="#A2EEE2", format="{artist}", padding=0),
                Spotify(format=" {track}"),
                widget.Spacer(),
                widget.ThermalZone(format_crit="{temp}°C", crit=80, high=60),
                widget.CPU(format="cpu:{load_percent}%"),
                widget.Memory(
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("alacritty -e htop")
                    },
                    format="mem:{MemUsed:.2f}G",
                    measure_mem="G",
                ),
                widget.Battery(
                    format="bat:{percent:2.0%}",
                    show_short_text=False,
                    update_interval=20,
                    low_percentage=0.2,
                    low_foreground="FF0000",
                    notify_below=20,
                ),
                widget.Volume(
                    fmt="vol:{}",
                    mouse_callbacks={
                        "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
                        "Button1": lambda: qtile.cmd_spawn(
                            "pactl set-sink-mute 0 toggle"
                        ),
                    },
                ),
                widget.Clock(format="%H:%M %A, %d %B"),
                widget.Systray(),
                widget.Sep(linewidth=0, padding=4),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
# Cringe, but needed to run apps such as Android-Studio :,)
wmname = "LG3D"
