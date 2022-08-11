from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True),
            24,
            background="#00000000",
            margin=[2, 0, 0, 0],
        ),
    ),
    Screen(
        top=bar.Bar(
            # Use everything except the systray, which would crash
            get_widgets(primary=False),
            24,
            background="#00000000",
            margin=[2, 0, 0, 0],
        )
    ),
]