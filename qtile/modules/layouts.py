from libqtile import layout
from libqtile.config import Match

# LAYOUTS
catppuccin = {
    "flamingo": "#F2CDCD",
    "mauve": "#DDB6F2",
    "pink": "#F5C2E7",
    "maroon": "#E8A2AF",
    "red": "#F28FAD",
    "peach": "#F8BD96",
    "yellow": "#FAE3B0",
    "green": "#ABE9B3",
    "teal": "#B5E8E0",
    "blue": "92CDFB",
    "sky": "#89DCEB",
    "white": "#D9E0EE",
    "gray0": "#6E6C7E",
    "black1": "#1A1826",
}

rose_pine = {
    "bg": "#1f1d2e",
    "fg": "#e0def4",
    "fg_gutter": "#555169",
    "black": "#191724",
    "red": "#eb6f92",
    "green": "#31748f",
    "yellow": "#f6c177",
    "blue": "#9ccfd8",
    "magenta": "#c4a7e7",
    "cyan": "#555169",
    "white": "#e0def4",
    "orange": "#6e6a86",
    "pink": "#2a2837"
}
colors = rose_pine

default_layout_config = {
    "border_focus": '#5294e2',
    "border_normal": '#2c5380',
    "border_width": 2,
    "margin": 2,
}

layouts = [
    layout.Columns(**default_layout_config),
    layout.MonadTall(**default_layout_config),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(**default_layout_config),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

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