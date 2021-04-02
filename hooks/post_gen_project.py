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


folders = OrderedDict()

folders['tasks'] = {
    'question': '\nShould it have tasks? ',
    'hint': '  Add task name i.e (Install packages) ',
    'action': '- name: {}\n  # TODO\n\n'
}

folders['handlers'] = {
    'question': '\nShould it have handlers?',
    'hint': '  Add handler name i.e (Restart uwsgi) ',
    'action': '- name: {}\n  # TODO\n\n'
}

folders['defaults'] = {
    'question': '\nIt should contain default variables?: ',
    'hint': '  Add variable i.e (operator: drunken_master) ',
    'action': '{}\n\n'
}

folders['meta'] = {
    'question': '\nShould it have meta info? ',
    'pre_hint': ' - Should it have dependencies? ',
    'pre_action': '\ndependencies:\n',
    'hint': '    Add dependency i.e ({role: aptsupercow, var: \'value\'}) ',
    'action': '  - {}\n'
}

folders['templates'] = {
    'question': '\nShould it have templates? ',
}

folders['files'] = {
    'question': '\nShould it have files? ',
}


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


def configure_role():
    print('\n\nROLE CONFIGURATION:\n===================')
    for folder_name, folder in folders.items():
        if read_user_yes_no(folder['question'], default_value=u'yes'):

            try:
                # this file has to be there, git doesn't store empty folders.
                os.remove(os.path.join(folder_name, '.empty'))
            except OSError:
                pass

            if 'hint' in folder:
                with open('{}/main.yml'.format(folder_name), 'a') as fp:

                    if 'pre_hint' in folder:
                        if read_user_yes_no(folder['pre_hint'], default_value=u'yes'):
                            fp.write(folder['pre_action'])
                        else:
                            continue

                    action_name = input(folder['hint'])
                    while action_name:
                        fp.write(folder['action'].format(action_name))
                        action_name = input(folder['hint'])

        else:
            shutil.rmtree(folder_name)

    if '{{ cookiecutter.add_travis_config }}' == 'n':
        os.remove('.travis.yml')

    if '{{ cookiecutter.add_Gitlab_CI_config }}' == 'n':
        os.remove('.gitlab-ci.yml')

    subprocess_cmd('git init')
    subprocess_cmd('git add .')
    subprocess_cmd('pre-commit install')
    subprocess_cmd('git commit -a -m "Initial commit by cookiecutter"')

    print("Path to your new role in the local machine is " + os.getcwd())


if __name__ == '__main__':
    configure_role()
