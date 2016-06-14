#!/usr/bin/env python
from configure.configure import *


def run_p2020_identity():
    os.system('echo -e "\n--------------------------\nP2020 IDM LIB: START\n"')
    git_clone_cmd = 'git clone '
    pip_cmd = 'pip install -e '
    nohup_cmd = '' if nohup_cmd_global is None else nohup_cmd_global + ' '
    git_url_splitted = git_idm_python_url.split('//')
    git_url_splitted_by_slash = git_idm_python_url.split('/')
    git_project_name = git_url_splitted_by_slash[-1].split('.')[0]

    if not os.path.isdir(project_folder + '/' + git_project_name):
        if git_user is None or git_password is None:
            if os.system(nohup_cmd + git_clone_cmd + git_idm_python_url + ' ' + project_folder + '/' + git_project_name) != 0:
                os.system('echo -e "\n******************\nP2020 IDM LIB: FAILED GIT PROCESS!\n"')
                sys.exit(1)
        else:
            if os.system(nohup_cmd + git_clone_cmd + git_url_splitted[0] + '//' + git_user + ':' + git_password + '@' +
                      git_url_splitted[1] + ' ' + project_folder + '/' + git_project_name) != 0:
                os.system('echo -e "\n******************\nP2020 IDM LIB: FAILED GIT PROCESS!\n"')
                sys.exit(1)
    else:
        print 'P2020 IDM REPOSITORY ALREADY EXISTS'

    if os.system(nohup_cmd + pip_cmd + project_folder + '/' + git_project_name + ' --user numpy') != 0:
        os.system('echo -e "\n******************\nP2020 IDM LIB: FAILED!\n"')
        sys.exit(1)

    os.system('echo -e "\nP2020 IDM LIB: DONE\n--------------------------\n"')


if __name__ == '__main__':
    run_p2020_identity()
