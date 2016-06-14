#!/usr/bin/env python
from configure.configure import *


def run_functional():
    os.system('echo -e "\n--------------------------\nFUNCTIONAL SERVICE: START\n"')
    git_clone_cmd = 'git clone '
    nohup_cmd = '' if nohup_cmd_global is None else nohup_cmd_global + ' '
    git_url_splitted = git_functional_url.split('//')
    git_url_splitted_by_slash = git_functional_url.split('/')
    git_project_name = git_url_splitted_by_slash[-1].split('.')[0]

    if not os.path.isdir(project_folder + '/' + git_project_name):
        if git_user is None or git_password is None:
            if os.system(nohup_cmd + git_clone_cmd + git_functional_url + ' ' + project_folder + '/' + git_project_name) != 0:
                os.system('echo -e "\n******************\nFUNCTIONAL SERVICE: FAILED GIT PROCESS!\n"')
                sys.exit(1)
        else:
            if os.system(nohup_cmd + git_clone_cmd + git_url_splitted[0] + '//' + git_user + ':' + git_password + '@' +
                      git_url_splitted[1] + ' ' + project_folder + '/' + git_project_name) != 0:
                os.system('echo -e "\n******************\nFUNCTIONAL SERVICE: FAILED GIT PROCESS!\n"')
                sys.exit(1)
    else:
        print 'FUNCTIONAL REPOSITORY ALREADY EXISTS'

    proc = subprocess.Popen(nohup_cmd + python_exec_cmd + ' ' + project_folder + '/' + git_project_name +
              '/functional/service/serviceWeb_tester.py',shell=True)

    os.system('echo -e "\nFUNCTIONAL SERVICE: DONE\n--------------------------\n"')

    return {'name': 'serviceWeb_tester.py', 'pid': proc.pid}


if __name__ == '__main__':
    from configure.utils import init_folders
    init_folders(project_folder)
    run_functional()
