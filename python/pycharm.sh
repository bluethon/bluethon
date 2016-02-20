#!/bin/bash

# change to your location
IDEA_HOME=/home/blue/pycharm-community-5.0.4

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Note: Can modify $IDEA_HOME/bin/idea{,64}.vmoptions
#       instead of setting here.
# "-Dawt.useSystemAAFontSettings=on" seems worse to me
# "-Dsun.java2d.xrender=true" makes fonts darker
# export _JAVA_OPTIONS="-Dawt.useSystemAAFontSettings=lcd \
export _JAVA_OPTIONS="-Dawt.useSystemAAFontSettings=on \
                          -Dsun.java2d.xrender=true"

# Having this set makes menu font size smaller (wtf?)
export GNOME_DESKTOP_SESSION_ID=this-is-deprecated
# unset GNOME_DESKTOP_SESSION_ID

exec $IDEA_HOME/bin/pycharm.sh "$@"
