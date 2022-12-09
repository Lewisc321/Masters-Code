# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:23:19 2022

@author: Callum Manning

Strath Uni - 201720173
"""
#My Modules
from LinkSetUp import *

#Show browser
HIDE_BROWSER = False

#User_Credentials
DVWAUSER = 'admin';
DVWAPASS = 'password';

#Link Options
URL_OPTIONS = [URL_HOST, URL_VM]
USING_VM = 0;
LOGIN = URL_OPTIONS[USING_VM] + LOGIN_EXT
USING_KALI = 0;


RANDOM_START_BRUTE_FORCE = True;

#SQLI attacks
USE_GENERATED_ATTACKS = True

#SQLI FOLDER
SQLI_FOLDER = './SQLIATTACKS/'

#COMSI FOLDER
COMSI_FOLDER = './COMSIATTACKS/'

#Brute Force Folder
BRUTE_FORCE_FOLDER = './BRUTEFORCEATTACKS/'


ABSOLUTE_NUMBERING = True;

#Browser Links
CHROME_LOC = './Drivers/chromedriver'
FIREFOX_LOC ='./Drivers/geckodriver'

#Choice of Browser 1 for chrome, 0 for firefox
BROWSER_CHOICE = 1;

#Sudo password
SUDO_PASS = ''

#Labelling
USER_LABEL = ''
SQLI_LABEL = 'sqli'
COMI_LABEL = 'comsi'
BRUTE_LABEL = 'brute_force'
LEVEL_LABELS = ['easy', 'medium', 'hard', 'impossible']
PASS_FAIL_LABEL = ['p', 'f']

#Iterations 
EASY_PASS= 3
MED_PASS = 3
HARD_PASS = 4

MED_FAIL = 3
HARD_FAIL = 3
IMPOSS_FAIL = 4