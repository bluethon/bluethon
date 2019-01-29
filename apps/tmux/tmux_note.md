Tmux Notes
==========

REFERENCE
---------

> <https://tylercipriani.com/blog/2013/09/12/important-lines-in-my-tmux/>
> <https://github.com/thcipriani/dotfiles/blob/master/tmux.conf>

CMD
---

    ctrl-b "                                horizon
    ctrl-b %                                vertical
    ctrl-b d                                detach
    ctrl-b arrow                            move to pane
    ctrl-b space                            next-layout(循环切换窗口布局)
    ctrl-b M-1 to M-5                       5种布局(OSX: Meta is Esc, iTerm2: Option)
    tmux ls                                 ls
    tmux attch-session -t <session-id>      go session
    tmux a #                                go last session
    tmux new -s <session name>              new seesion with name
    tmux a -t <name>
    tmux kill-session -t [name of session]
