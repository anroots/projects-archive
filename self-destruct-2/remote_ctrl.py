#!/usr/bin/env python

# A listerner that fetches commands from an URL and executes them.
# Runs until forced to quit.
# Author Ando Roots 2011

import threading
import urllib
import urllib2
import shlex
import subprocess

# CONFIG - CHANGEME!
COMMAND_URL = 'http://ando.roots.ee/remote_ctrl/controller.php'
MODE = 'DEFINED' # LITERAL (run incoming commands as they are) or DEFINED (treat as keywords)
COMMANDS = {'now': 'date',
            'do': './run_program.sh'} # Only fill if MODE = DEFINED
INTERVAL = 2 # Check frequency, in seconds

# END OF CONFIG
acknowledge_status = 'OK'


def listen():
    t = threading.Timer(INTERVAL, periodic)
    t.start()
    print 'Initiating listening sequence. System on standby...'
    

def periodic():
    global t
    global acknowledge_status
    command = get_command()
    if (len(command) > 0):
        print 'New instruction:', command
        run_command(command)
        send_acknowledge()
        print 'Instruction executed. Status: ' + str(acknowledge_status) + ' System on standby...'
    t = threading.Timer(INTERVAL, periodic)
    t.start()
 

def run_command(command):
    if (MODE == 'LITERAL'):
        run_it(command)
    else:
        if (command in COMMANDS):
            run_it(COMMANDS[command])
        else:
            print 'Command',command,'not found in defined list.'
    

def run_it(command):
    args = shlex.split(command)
    code = subprocess.Popen(args,stdout=subprocess.PIPE)
    out, err = code.communicate()
    print out
    

def get_command():
    return urllib.urlopen(COMMAND_URL).read()


def send_acknowledge():
    values = {'acknowledge' : 'yes'}
    data = urllib.urlencode(values)
    api_url = COMMAND_URL + '?' + data
    acknowledge_status = urllib.urlopen(api_url).read()


if __name__ == '__main__':
    listen()