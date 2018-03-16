#!/bin/bash

# alias
git config alias.st status
git config alias.cm commit
git config alias.co checkout
git config alias.ps push
git config alias.pl pull
git config alias.cmp '!f() { git add -A && git commit -m "$*" && git push; }; f'

# vim
git config core.editor vim
git config push.default vim
