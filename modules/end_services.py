#!/usr/bin/env python
import os


def end_python_services():
    flag = True
    while flag:
        print "1: KILL ALL SERVICES"
        print "0: EXIT"
        cmd = raw_input('Type the command that you want to execute:')
        try:
            if cmd == '0':
                flag = False
                print "Exit!"
                os._exit(0)
            else:
                print 'Services down!'
                os.system('pkill -9 python')
                os._exit(0)
        except:
            print 'Invalid command!'

if __name__ == '__main__':
    end_python_services()