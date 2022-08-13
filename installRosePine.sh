#!/bin/bash

echo "INSTALLING ROSE-PINE-GTK"
wget https://github.com/rose-pine/gtk/releases/download/v2.0.0/AllRosePineThemesGTK.tar.gz
wget https://github.com/rose-pine/gtk/releases/download/v2.0.0/AllRosePineThemesIcons.tar.gz

tar xf AllRosePineThemesGTK.tar.gz
tar xf AllRosePineThemesIcons.tar.gz
rm AllRosePineThemesGTK.tar.gz
rm AllRosePineThemesIcons.tar.gz

sudo cp -r AllRosePineThemesGTK/rose-pine-gtk /usr/share/themes
sudo cp -r AllRosePineThemesIcons/rose-pine-icons /usr/share/icons

rm -rf AllRosePineThemesGTK
rm -rf AllRosePineThemesIcons
