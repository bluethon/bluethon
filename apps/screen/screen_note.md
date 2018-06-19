Linux Screen Note
=================

CMD
---

``` shell
screen -ls                  # 查看所有session
screen -S 10260.pts-21.blue-ThinkPad-T430s  -X quit
                            #不登入, 结束
screen -r
```

Key
---

    c+a c+a             # 循环切换

### process background

``` shell
screen                      # first
netease-cloud-music %U      # run
# C+a & C+d
screen -ls                  # list
screen -r foo               # attach
```

Ctrl+A and Ctrl+D, and session后台运行
