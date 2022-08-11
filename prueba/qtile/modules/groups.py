from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod

# WORKSPACES
groups = [ Group(f"{i+1}", label="") for i in range(9)]
group_hotkeys = "123456789"
#  groups = [
    #  Group("1", label=""),
    #  Group("2", label=""),
    #  Group("3", label=""),
    #  #  Group(
        #  #  "3",
        #  #  label="",
        #  #  matches=[
            #  #  Match(wm_class=["zoom"]),
        #  #  ],
    #  #  ),
    #  Group("4", label=""),
    #  Group("5", label="")
#  ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
