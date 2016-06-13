#!/usr/bin/env python
from configure.configure import *


def run_middle():
    print 'CLONING MIDDLE REPOSITORY: PROCESS START'
    git_clone_cmd = 'git clone '
    git_url_splitted = git_middle_url.split('//')
    git_url_splitted_by_slash = git_middle_url.split('/')
    git_project_name = git_url_splitted_by_slash[-1].split('.')[0]

    if not os.path.isdir(project_folder + '/' + git_project_name):
        if git_user is None or git_password is None:
            os.system(git_clone_cmd + git_middle_url + ' ' + project_folder + '/' + git_project_name)
        else:
            os.system(git_clone_cmd + git_url_splitted[0] + '//' + git_user + ':' + git_password + '@' +
                  git_url_splitted[1] + ' ' + project_folder + '/' + git_project_name)
    else:
        print 'MIDDLE REPOSITORY ALREADY EXISTS'

    os.system(python_exec_cmd + ' ' + project_folder + '/' + git_project_name + '/middle_service/middle.py &')
    print 'CLONING MIDDLE REPOSITORY: PROCESS DONE'

if __name__ == '__main__':
    from configure.utils import init_folders
    init_folders(project_folder)
    run_middle()
