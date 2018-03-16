#!/bin/bash

# http://stackoverflow.com/a/35049625/4757521

# alias
git config --global alias.st status
git config --global alias.cm commit
git config --global alias.co checkout
git config --global alias.ps push
git config --global alias.pl pull
git config --global alias.cmp "!f() { git add -A && git commit -m \"$@\" && git push; }; f"

# vim
git config --global core.editor vim
