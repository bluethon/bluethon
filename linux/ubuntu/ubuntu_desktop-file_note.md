Ubuntu Desktop File Note
========================

path
----

    /usr/share/applications/*.desktop
    ~/.local/share/applications/*.desktop


validate file
-------------

    desktop-file-validate ~/.local/share/applications/*.desktop

install
-------

move to `/usr/share/applications` and reload unity

    desktop-file-install foo.desktop


> <http://askubuntu.com/questions/501880/applications-dont-appear-in-the-dash-14-04?noredirect=1&lq=1>
> <https://help.ubuntu.com/community/UnityLaunchersAndDesktopFiles>
