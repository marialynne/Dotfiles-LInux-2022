"""
# AUTOSTART
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])







from modules.screens import screens



"""

import os
import subprocess 
from modules.groups import groups
from modules.keys import keys, mod
from modules.layouts import layouts, floating_layout, colors
from modules.mouse import mouse
from modules.hooks import *

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal






# PANEL

widget_defaults = dict(
    font = "JetBrainsMono Nerd Font",
    fontsize = 16,
    padding = 3,
    foreground = "#000000",
)
extension_defaults = widget_defaults.copy()


def get_widgets(primary=False):
    widgets = [
        widget.TextBox(
            text = "    ",
            fontsize = 20,
            padding = 0,
            mouse_callbacks = {"Button1": lazy.spawn("rofi -show drun")},
            background = colors["magenta"],
            foreground = colors["black"]
        ),
        widget.TextBox(
            text = "",
            padding = 0,
            fontsize = 30,
            foreground = colors["black"],
            background = colors["magenta"],
        ),
        widget.CurrentLayoutIcon(
            scale=0.5,
            foreground = colors["white"],
            background = colors["black"],),
        widget.GroupBox(
            foreground = colors["cyan"],
            highlight_method = "text",
            block_highlight_text_color = colors["white"],
            active = colors["fg"],
            inactive = colors["cyan"],
            rounded = False,
            highlight_color = [colors["fg"], colors["yellow"]],
            urgent_alert_method = "line",
            urgent_text = colors["red"],
            urgent_border = colors["red"],
            disable_drag = True,
            use_mouse_wheel = False,
            hide_unused = False,
            spacing = 5,
            this_current_screen_border = colors["yellow"],
            background = colors["black"],
            fontsize = 14
        ),
        widget.TextBox(
            text = " ",
            padding = 0,
            fontsize = 30,
            foreground = colors["fg_gutter"],
            background = colors["black"],
        ),
        widget.WindowName(
            font = 'Comic Code',
            fontsize = 14,
            padding = 3,
            format = '{state}{name}',
            foreground = colors["white"],
            background = colors["fg_gutter"],
            center_aligned = True
        ),
        widget.Wallpaper(
            directory = '/home/manu320/.config/wallpapers/',
            random_selection = True,
            fmt='  ',
            foreground = colors["white"],
            background = colors["fg_gutter"],
        ),
        widget.PulseVolume(
            fmt = "墳 {} ",
            mute_command = "amixer -D pulse set Master toggle",
            foreground = colors["white"],
            background = colors["fg_gutter"],
        ),
        widget.TextBox(
            text = "",
            padding = 0,
            fontsize = 30,
            foreground = colors["yellow"],
            background = colors["fg_gutter"],
        ),
        widget.CPU(
            format=" {load_percent:04}% ",
            mouse_callbacks={"Button1": lazy.spawn("kitty -e htop")},
            background = colors["yellow"],
            foreground = colors["bg"],
            font = 'Comic Code',
            fontsize = 14,
        ),
        widget.Memory(
            format = '{MemUsed: .0f}{mm}/{MemTotal:.0f}{mm} ',
            padding = 0,
            measure_mem = 'G',
            measure_swap = 'G',
            foreground = colors["black"],
            background = colors["yellow"],
            font = 'Comic Code',
            fontsize = 14,
        ),
        widget.TextBox(
            text = "",
            padding = 0,
            fontsize = 30,
            foreground = colors["magenta"],
            background = colors["yellow"],
        ),
        widget.Battery(
            format = "{char} {percent:2.0%} ",
            charge_char = "",
            discharge_char = "",
            full_char = "",
            unknown_char = "",
            empty_char = "",
            show_short_text = False,
            background = colors["magenta"],
            font = 'Comic Code',
            fontsize = 14,
        ),
        widget.ThermalZone(
            format=' {temp}°C',
            format_crit = '{temp}°C',
            crit = 60,
            high = 40,
            fgcolor_crit = 'ff0000',
            fgcolor_high = 'ffaa00',
            fgcolor_normal= '000000',
            background = colors["magenta"],
            font = 'Comic Code',
            fontsize = 14,
        ),
        widget.NvidiaSensors(
            format = '| {temp}°C ',
            threshold=  68,
            foreground_alert = 'ff6000',
            foreground = "000000",
            background = colors["magenta"],
            font = 'Comic Code',
            fontsize = 14,
        ),
        widget.TextBox(
            text = "",
            padding = 0,
            fontsize = 30,
            foreground = colors["pink"],
            background = colors["magenta"],
        ),
        widget.Clock(
            format="%d/%m/%y - %I:%M %p ", 
            foreground = colors["white"],
            background = colors["pink"],
            font = 'Comic Code',
            fontsize = 14,
        ),
    ]
    if primary:
        widgets.insert(6, widget.Systray(padding=5))
    return widgets


screens = [
    Screen(
        top = bar.Bar(
            get_widgets(primary = True),
            30,
            background = colors["fg_gutter"],
            margin=[4, 4, 2, 4],
        ),
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
    Screen(
        top = bar.Bar(
            # Use everything except the systray, which would crash
            get_widgets(primary = False),
            30,
            background="#00000000",
            margin=[4, 4, 2, 4],
        ),
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    )
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
focus_on_window_activation = "smart"
wmname = "Qtile"


