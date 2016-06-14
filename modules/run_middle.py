#!/usr/bin/env python
from configure.configure import *


def run_middle():
    os.system('echo -e "\n--------------------------\nMIDDLE SERVICE: START\n"')
    git_clone_cmd = 'git clone '
    nohup_cmd = '' if nohup_cmd_global is None else nohup_cmd_global + ' '
    git_url_splitted = git_middle_url.split('//')
    git_url_splitted_by_slash = git_middle_url.split('/')
    git_project_name = git_url_splitted_by_slash[-1].split('.')[0]

    if not os.path.isdir(project_folder + '/' + git_project_name):
        if git_user is None or git_password is None:
            if os.system(nohup_cmd + git_clone_cmd + git_middle_url + ' ' + project_folder + '/' + git_project_name) != 0:
                os.system('echo -e "\n******************\nMIDDLE SERVICE: FAILED GIT PROCESS!\n"')
                sys.exit(1)
        else:
            if os.system(nohup_cmd + git_clone_cmd + git_url_splitted[0] + '//' + git_user + ':' + git_password + '@' +
                  git_url_splitted[1] + ' ' + project_folder + '/' + git_project_name) != 0:
                os.system('echo -e "\n******************\nMIDDLE SERVICE: FAILED GIT PROCESS!\n"')
                sys.exit(1)
    else:
        print 'MIDDLE REPOSITORY ALREADY EXISTS'

    proc = subprocess.Popen(nohup_cmd + python_exec_cmd + ' ' + project_folder + '/' + git_project_name +
              '/middle_service/middle.py',shell=True)

    os.system('echo -e "\nMIDDLE SERVICE: DONE\n--------------------------\n"')

    return {'name': 'middle.py', 'pid': proc.pid}

if __name__ == '__main__':
    from configure.utils import init_folders
    init_folders(project_folder)
    run_middle()
