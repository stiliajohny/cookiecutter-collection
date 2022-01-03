#!/usr/bin/env python3

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


def configure_role():

    print("\n")
    print("Path to your new role in the local machine is " + os.getcwd())


if __name__ == '__main__':
    configure_role()
