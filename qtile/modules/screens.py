from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import os

screens = [
    Screen(
        top=bar.Bar(
            [   
                #widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show app")}),
                widget.GroupBox(
                                ),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.Systray(icon_size = 20),    
                
            ],
            30,  # height in px
            background="#404552"  # background color
        ), ),
]
