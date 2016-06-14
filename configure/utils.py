import os
import subprocess
import sys

# Get the correct value from the .cfg file
def resolve_config_parameters(config_parser, head, parameter, value=0):
    item = config_parser.get(head, parameter, value)

    if item is not None and item != "":
        return item

    return None


# Check if the path exist, if so, remove it, then create it again, for make sure that the folder is clean
def init_folders(path):
    cmd_rm = 'rm -rf '
    if os.path.isdir(path):
        os.system(cmd_rm + path)
        os.makedirs(path, True)
    else:
        os.makedirs(path, True)

    return os.path.isdir(path)


def kill_services(pids):
    for pid in pids:
        subprocess.call('kill -9 ' + str(pid['pid']), shell=True)
    print 'Process successfully killed'

