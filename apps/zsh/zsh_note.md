# Zsh Note

## autojump

``` sh
# install
brew install autojump
# add to .zshrc(maybe different)
[ -f /usr/local/etc/profile.d/autojump.sh ] && . /usr/local/etc/profile.d/autojump.sh

# use
j -s        # status
```

## .zshrc

``` sh
# 直接打开后缀文件
alias -s zip='unzip'

# bindkey
bindkey ^F forward-word
bindkey ^B backward-word

# docker
alias de='docker exec -i -t'
alias dl='docker logs -tf'
alias ds='docker stats'
alias dis='docker images'
alias dip='docker image prune --filter until=48h'
alias dps='docker ps -a --format="table {{.Names}}\t{{.Image}}\t{{.RunningFor}}\t{{.Status}}\t{{.Ports}}"'
alias dsp='docker system prune --filter until=48h'
alias dvs='docker volume ls'
alias drmi='docker rmi'
alias dcu='docker-compose up -d'

# time
# at the begining
zmodload zsh/zprof
# at end
zprof
```
