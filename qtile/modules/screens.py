from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import os

# SCREENS 
screens = [
    Screen(
        top = bar.Bar(
            get_widgets(primary = True),
            30,
            background = colors["fg_gutter"],
            margin=[0, 0, 0, 0],
        ),
    ),
    Screen(
        top = bar.Bar(
            # Use everything except the systray, which would crash
            get_widgets(primary = False),
            30,
            background="#00000000",
            margin=[0, 0, 0, 0],
        )
    )
]
