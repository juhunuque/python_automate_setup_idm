
## Pre-Requirements
All scripts below make the following assumptions:
- You have already installed 2.x (2.7 or later) or 3.x (3.4 or later)
- You are using pip for dependency management
- You have GCC in your environment
- You have installed Python Development packages
- Git in your environment 

## Configuring the settings
First up, you should configure the environment parameters, you will find a file 'settings.cfg' inside the config folder.
If you want to clone the projects by using SSH urls, you must to leave the fields GIT_USER and GIT_PASSWORD in blank.
Otherwise, if you will use HTTP urls, you must fill those fields.

When you have already configured the 'settings.cfg' you can proceed with the next part. 

## Using the script
The file 'run.py', executes all the modules of the project (Install the library, clone the projects, etc), so maybe that 
file is what are you looking for.
In order to use it as a shell script, you first need to give it the right permissions. Run this:
```sh
    $ chmod u+x run.py
```

Note: If you want to execute any module independently, you must to run the previous command for each desired script.

Now, run the master file as a shell script by executing the following script:

```sh
    $ sudo ./run.py
```
Note: You must execute it as root user
The script will start to execute all the required tasks:
- Install required libraries
- Configure environment variables
- Clone and install P2020 Identity library
- Clone and execute Target Service
- Clone and execute Middle Service
- Clone and execute Functional Service

At the end of the process, the script will ask you if you want to kill the services. If you want so, just type 1.
But if you want to kill them later, you can manually run the module 'end_services.py' later.
Or you can use this shell script in order to kill all the python processes:
```sh
    $ sudo pkill -9 python
```


## Extra notes
If you need to install someone of the requirements, you can refer to the following links (They are for CentOs, if you are 
using another OS, please check for the correct documentation)
### PIP IN CENTOS: 
http://www.liquidweb.com/kb/how-to-install-pip-on-centos-7/
- curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
- python get-pip.py

### GCC: 
http://www.cyberciti.biz/faq/centos-rhel-7-redhat-linux-install-gcc-compiler-development-tools

###  INSTALL PYTHON DEV: 
http://stackoverflow.com/questions/11094718/error-command-gcc-failed-with-exit-status-1-while-installing-eventlet
- sudo yum install python-devel
- sudo yum install libevent-devel
- easy_install gevent
- yum install libffi-devel

## Important shell commands
- chmod u+x <file_name>: Grant permissions
- pkill -9 python: Kill python processes

