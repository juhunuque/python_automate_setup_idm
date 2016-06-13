#!/usr/bin/env python
from configure.configure import *


def run_p2020_identity():
    print 'INSTALLING P2020 IDENTITY: PROCESS START'
    git_clone_cmd = 'git clone '
    pip_cmd = 'pip install -e '
    git_url_splitted = git_idm_python_url.split('//')
    git_url_splitted_by_slash = git_idm_python_url.split('/')
    git_project_name = git_url_splitted_by_slash[-1].split('.')[0]

    os.system('pip uninstall platform2020-identity')
    if not os.path.isdir(project_folder + '/' + git_project_name):
        if git_user is None or git_password is None:
            os.system(git_clone_cmd + git_idm_python_url + ' ' + project_folder + '/' + git_project_name)
        else:
            os.system(git_clone_cmd + git_url_splitted[0] + '//' + git_user + ':' + git_password + '@' +
                      git_url_splitted[1] + ' ' + project_folder + '/' + git_project_name)
    else:
        print 'P2020 IDM REPOSITORY ALREADY EXISTS'

    os.system(pip_cmd + project_folder + '/' + git_project_name)
    print 'INSTALLING P2020 IDENTITY: PROCESS DONE'


if __name__ == '__main__':
    run_p2020_identity()
