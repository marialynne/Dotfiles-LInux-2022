#!/bin/sh
picom &  disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed
setxkbmap latam & disown # Layout keyboard LATAM
dunst & disown 
blueman-applet & disown
nm-applet & disown
xfce4-clipman & disown
xclip & disown
#discord & disown

ln $HOME/.config/starship.toml $STARSHIP

