# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:02:30 2022

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


if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SQLI_FOLDER)
    
for i in range(1,EASY_PASS+1):
    #Click SQLI link 
    clickLink_XPATH(browser, SQL_INJECTION_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[0],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[0],PASS_FAIL_LABEL[0]])
        p = startPcap(SQLI_FOLDER,PcapName)
        
    #Sql injection Low level attack
    SQLI_LOW_LEVEL(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
    

time.sleep(3)



#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Medium')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SQLI_FOLDER)

for i in range(1, MED_PASS+1):
    #Click SQLI link 
    clickLink_XPATH(browser, SQL_INJECTION_XPATH)
    
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([SQLI_FOLDER, i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[0]])
        p = startPcap(SQLI_FOLDER,PcapName)
        
    #Sql injection Mid level attack
    SQLI_MID_LEVEL(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


time.sleep(3)

#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'High')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SQLI_FOLDER)

for i in range(1, HARD_PASS+1):

    
    #Click SQLI link 
    clickLink_XPATH(browser, SQL_INJECTION_XPATH)
    
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[0]])
        p = startPcap(SQLI_FOLDER,PcapName)
    
    #High Level SQL attack
    SQLI_HIGH_LEVEL(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


time.sleep(3)

#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Medium')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SQLI_FOLDER)

print(MED_FAIL_WARNING)

for i in range(1, MED_FAIL+1):
    #Click SQLI link 
    clickLink_XPATH(browser, SQL_INJECTION_XPATH)
    
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[1]])
        p = startPcap(SQLI_FOLDER,PcapName)
        
    #Sql injection Mid level attack
    SQLI_LOW_LEVEL(browser)
    
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


time.sleep(3)



#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'High')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SQLI_FOLDER)

print(HARD_FAIL_WARNING)

for i in range(1, HARD_FAIL+1):

    
    #Click SQLI link 
    clickLink_XPATH(browser, SQL_INJECTION_XPATH)
    
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([ currentNumb + i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([ i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[1]])
        p = startPcap(SQLI_FOLDER,PcapName)
        
    #High Level SQL attack
    SQLI_LOW_LEVEL(browser)
    
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


time.sleep(3)





#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Impossible')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SQLI_FOLDER)

print(IMPOSS_FAIL_WARNING)

for i in range(1, IMPOSS_FAIL+1):

    
    #Click SQLI link 
    clickLink_XPATH(browser, SQL_INJECTION_XPATH)
    
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([ currentNumb + i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[3],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,SQLI_LABEL, LEVEL_LABELS[3],PASS_FAIL_LABEL[1]])
        p = startPcap(SQLI_FOLDER,PcapName)
    
        
    #High Level SQL attack
    SQLI_LOW_LEVEL(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)



