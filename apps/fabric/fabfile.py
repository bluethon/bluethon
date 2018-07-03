import logging
import os

from fabric import Connection
from invoke import Responder, task

BASE_DIR = os.path.dirname(__file__)

logging.basicConfig(level=logging.INFO)


def ohmyzsh(con):
    responder = Responder(
        pattern=r'Password: ',
        response=con.config.sudo.password + '\n'
    )
    exit_responder = Responder(
        pattern=r'➜.*~.*',
        response='exit\n'
    )
    con.sudo('apt-get install zsh -y')
    con.run('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"',
            pty=True,
            watchers=[responder, exit_responder])
    con.run('sed -i -- "s/robbyrussell/ys/" ~/.zshrc')


def reset(con):
    """ 重置$SHELL """
    con.sudo('chsh -s /bin/bash pt')
    con.run('rm -rf .oh-my-zsh/')


@task
def rm(context):
    for host in context.config.hosts:
        con = Connection(host, config=context.config)
        reset(con)
        print(con)