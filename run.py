#!/usr/bin/env python
from configure.configure import *
from configure.utils import kill_services, check_process_running

# Install required libraries
nohup_cmd = '' if nohup_cmd_global is None else nohup_cmd_global + ' '
pid_codes = []
os.system('echo -e "\n--------------------------\nINSTALLING DEPENDENCIES: START\n"')
if os.system(nohup_cmd + python_exec_cmd + ' configure/setup.py install --user') != 0:
    os.system('echo -e "\n******************\nINSTALLING DEPENDENCIES: FAILED!\n"')
    sys.exit(1)
os.system('echo -e "\nINSTALLING DEPENDENCIES: DONE\n--------------------------\n"')

# Configure Environment variables
from modules.run_env_variables import set_variables
set_variables()

# Initialize work folders
from configure.utils import init_folders
init_folders(project_folder)

# Install P2020 Identity Lib
from modules.run_p2020_identity import run_p2020_identity
run_p2020_identity()

# Cloning Target Repository
from modules.run_target import run_target
pid_codes.append(run_target())

# Cloning Middle Repository
from modules.run_middle import run_middle
pid_codes.append(run_middle())

# Cloning Functional Repository
from modules.run_functional import run_functional
pid_codes.append(run_functional())

time.sleep(5)
print '\n----------------\n Waiting for services...\n'

proc = subprocess.call(python_exec_cmd + ' ' + project_folder + '/platform2020-idm-python-functional-tester/functional/test_service/suite.py', shell=True)
kill_services(pid_codes)
sys.exit(proc)





