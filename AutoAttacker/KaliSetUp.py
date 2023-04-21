# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:20:52 2022

@author: Callum Manning

Strath Uni - 201720173


"""
from LinkSetUp import *
from UserSetUp import *
import subprocess

#Set up Kali, set up mysql and apache2.
def setUpKali(): 
   if USING_KALI:
        print(KALI_SET_UP_PRINT)
        
        cmd = ['sudo', 'service', 'mysql', 'start'];
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE)
        process.wait()
        cmd = ['sudo', 'service', 'apache2', 'start'];
        process = subprocess.Popen( cmd, stdout=subprocess.PIPE)
        process.wait()