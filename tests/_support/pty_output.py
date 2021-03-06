import sys

from invoke import run
from invoke.tasks import task


cmd = "echo foo && {0} err.py bar".format(sys.executable)


def _go(hide):
    run(cmd, hide=hide, pty=True)

@task
def hide_out():
    _go('out')

@task
def hide_err():
    _go('err')

@task
def hide_both():
    _go('both')
