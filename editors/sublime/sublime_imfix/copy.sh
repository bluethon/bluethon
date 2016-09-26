#!/bin/bash

path=$(/bin/pwd)

sudo cp $path/libsublime-imfix.so /opt/sublime_text/
sudo cp $path/subl /usr/bin/
sudo cp $path/sublime_text.desktop /usr/share/applications/
