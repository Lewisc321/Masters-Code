# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 02:59:44 2022

@author: Callum Manning

Strath Uni - 201720173


"""

#My Modules
from BrowserSetUp import *
from Pcap_Capture import *
from NameGenerator import *
from KaliSetUp import *

#Set up Kali settings 
setUpKali()

#Open Selenium browser
browser = openBrowser()

#Pull up DVWA login Page
browser.get(LOGIN)

#Login to DVWA
loginDVWA(browser)


if ABSOLUTE_NUMBERING and USING_VM:
    currentNumb = getAbsoluteNumber(COMSI_FOLDER)
    
for i in range(1,EASY_PASS+1):
    #Click Command Injection link 
    clickLink_XPATH(browser, COMMAND_INJECTION_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[0],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[0],PASS_FAIL_LABEL[0]])
        p = startPcap(COMSI_FOLDER, PcapName)
        
    #Command injection Low level attack
    COMSI_LOW_LEVEL(browser)

    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
    


#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Medium')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(COMSI_FOLDER)
time.sleep(1)
for i in range(1,MED_PASS+1):
    #Click Command Injection link 
    clickLink_XPATH(browser, COMMAND_INJECTION_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[0]])
        p = startPcap(COMSI_FOLDER, PcapName)
        
    #Command injection Mid level attack
    COMSI_MID_LEVEL(browser)

    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
        
time.sleep(3)

#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'High')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(COMSI_FOLDER)

for i in range(1,HARD_PASS+1):
    #Click Command Injection link 
    time.sleep(1)
    clickLink_XPATH(browser, COMMAND_INJECTION_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[0]])
        p = startPcap(COMSI_FOLDER, PcapName)
        
    #Command injection High level attack
    COMSI_HIGH_LEVEL(browser)

    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
        

time.sleep(3)

#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Medium')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(COMSI_FOLDER)

print(MED_FAIL_WARNING)

for i in range(1, MED_FAIL+1):
    #Click Command Injection link 
    clickLink_XPATH(browser, COMMAND_INJECTION_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[1]])
        p = startPcap(COMSI_FOLDER, PcapName)
        
    #Command injection Low level attack
    COMSI_LOW_LEVEL(browser)

    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
    
time.sleep(3)



#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'High')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(COMSI_FOLDER)

print(HARD_FAIL_WARNING)

for i in range(1, HARD_FAIL+1):
    #Click Command Injection link 
    clickLink_XPATH(browser, COMMAND_INJECTION_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[1]])
        p = startPcap(COMSI_FOLDER, PcapName)
        
    #Command injection Low level attack
    COMSI_LOW_LEVEL(browser)

    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
    
time.sleep(3)


#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Impossible')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(COMSI_FOLDER)

print(IMPOSS_FAIL_WARNING)

for i in range(1, IMPOSS_FAIL+1):

    #Click Command Injection link 
    clickLink_XPATH(browser, COMMAND_INJECTION_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[3],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,COMI_LABEL, LEVEL_LABELS[3],PASS_FAIL_LABEL[1]])
        p = startPcap(COMSI_FOLDER, PcapName)
        
    #Command injection Low level attack
    COMSI_LOW_LEVEL(browser)

    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
    
time.sleep(3)
