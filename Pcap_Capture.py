# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 17:34:25 2022

@author: Callum Manning

Strath Uni - 201720173
"""

#My Modules
from UserSetUp import *
from ExtModulesSetUp import *

def startPcap(pcapTitle):
    pcapTitle = SQLI_FOLDER + pcapTitle
    try:
        cmd1 = subprocess.Popen(['echo',SUDO_PASS], stdout=subprocess.PIPE)
        process = subprocess.Popen(['sudo', 'tcpdump','-i', 'lo', '-w', pcapTitle] , stdout=subprocess.PIPE, stdin =cmd1.stdout)
        time.sleep(1)
    except OSError as e:
        print(e)
    return process



def endPcap(process):
    try:
        time.sleep(1)
        cmd1 = subprocess.Popen(['echo',SUDO_PASS], stdout=subprocess.PIPE)
        end = subprocess.Popen(['sudo', 'killall', 'tcpdump', str(process.pid)] ,stdin=cmd1.stdout,  stdout=subprocess.PIPE)
        time.sleep(1)
        poll = process.poll()
        if poll is not None:
            cmd1 = subprocess.Popen(['echo',SUDO_PASS], stdout=subprocess.PIPE)
            end = subprocess.Popen(['sudo', 'kill', str(process.pid), '15'] ,stdin=cmd1.stdout,  stdout=subprocess.PIPE)
            time.sleep(1)
        
    except OSError as e:
        print(e)

