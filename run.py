#!/usr/bin/env python
import time
from configure.configure import *

# Install required libraries
os.system(python_exec_cmd + ' configure/setup.py install')

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
run_target()

# Cloning Middle Repository
from modules.run_middle import run_middle
run_middle()

# Cloning Functional Repository
from modules.run_functional import run_functional
run_functional()

# Code to turn off the services
time.sleep(2)
from modules.end_services import end_python_services
end_python_services()





