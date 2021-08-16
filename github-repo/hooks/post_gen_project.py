#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals, absolute_import, print_function
from collections import OrderedDict
from cookiecutter.prompt import read_user_yes_no

import os
import subprocess
import shutil


try:
    input = raw_input
except NameError:
    pass


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


def configure_repo():
    print('\n\nREPO CONFIGURATION:\n===================')
    substring = " "
    repo_name_fixed="{{cookiecutter.repo_name}}".replace(" ", "-")

    if substring in "{{cookiecutter.git_user}}":
        print("cookiecutter.git_user has a space character: '{{cookiecutter.git_user}}'")
        print("Current cookiecut will be deleted. Try again")
        shutil.rmtree(os.getcwd())
        exit()


    subprocess_cmd('git remote set-url origin git@github.com:' + "{{cookiecutter.git_user}}"  + '/' + repo_name_fixed + '.git')
    subprocess_cmd('git init')
    subprocess_cmd('git add .')
    subprocess_cmd('git commit -a -m "Initial commit by cookiecutter"')

    print("Path to your new repo in the local machine is " + os.getcwd())


if __name__ == '__main__':
    configure_repo()
