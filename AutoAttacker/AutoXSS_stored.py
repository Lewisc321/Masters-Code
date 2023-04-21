# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 03:02:41 2023

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
    currentNumb = getAbsoluteNumber(XSS_STORED_FOLDER)
    
for i in range(1,EASY_PASS+1):
    #Click SQLI link 
    elemPresenceCheck_XPATH(browser, XSS_STORED_XPATH)
    clickLink_XPATH(browser, XSS_STORED_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[0],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[0],PASS_FAIL_LABEL[0]])
        p = startPcap(XSS_STORED_FOLDER,PcapName)
        
    #Sql injection Low level attack
    XSS_STORED_ATTACK(browser, XSS_LEVEL[0])
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
        
    XSS_CATCH_CLEAR_BOOK(browser)
     

time.sleep(3)


#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Medium')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(XSS_STORED_FOLDER)
    

for i in range(1,MED_PASS+1):
    #Click SQLI link 
    elemPresenceCheck_XPATH(browser, XSS_STORED_XPATH)
    clickLink_XPATH(browser, XSS_STORED_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[0]])
        p = startPcap(XSS_STORED_FOLDER,PcapName)
        
    #Sql injection Low level attack
    XSS_STORED_ATTACK(browser, XSS_LEVEL[1])
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
        
    XSS_CATCH_CLEAR_BOOK(browser)
    

time.sleep(3)

    
#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'High')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(XSS_STORED_FOLDER)
    

for i in range(1,HARD_PASS+1):
    #Click SQLI link 
    elemPresenceCheck_XPATH(browser, XSS_STORED_XPATH)
    clickLink_XPATH(browser, XSS_STORED_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[0]])
        else:
            PcapName = nameFile([i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[0]])
        p = startPcap(XSS_STORED_FOLDER,PcapName)
        
    #Sql injection Low level attack
    XSS_STORED_ATTACK(browser, XSS_LEVEL[2])
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
        
    XSS_CATCH_CLEAR_BOOK(browser)


time.sleep(3)

#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Medium')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(XSS_STORED_FOLDER)

print(MED_FAIL_WARNING)

for i in range(1, MED_FAIL+1):
    #Click SQLI link 
    elemPresenceCheck_XPATH(browser, XSS_STORED_XPATH)
    clickLink_XPATH(browser, XSS_STORED_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[1],PASS_FAIL_LABEL[1]])
        p = startPcap(XSS_STORED_FOLDER,PcapName)
        
    #Sql injection Low level attack
    XSS_STORED_ATTACK(browser, XSS_LEVEL[0])
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)

time.sleep(3)




#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'High')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(XSS_STORED_FOLDER)

print(HARD_FAIL_WARNING)

for i in range(1, HARD_FAIL+1):
    #Click SQLI link 
    elemPresenceCheck_XPATH(browser, XSS_STORED_XPATH)
    clickLink_XPATH(browser, XSS_STORED_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[2],PASS_FAIL_LABEL[1]])
        p = startPcap(XSS_STORED_FOLDER,PcapName)
        
    #Sql injection Low level attack
    XSS_STORED_ATTACK(browser, XSS_LEVEL[1])
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)

time.sleep(3)



#Click the link to the security page
clickLink_XPATH(browser, DVWA_SECURITY_XPATH)

#Change to medium Security Level
changeSecurity(browser, 'Impossible')

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(XSS_STORED_FOLDER)

print(IMPOSS_FAIL_WARNING)

for i in range(1, IMPOSS_FAIL+1):
    #Click SQLI link
    elemPresenceCheck_XPATH(browser, XSS_STORED_XPATH) 
    clickLink_XPATH(browser, XSS_STORED_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[3],PASS_FAIL_LABEL[1]])
        else:
            PcapName = nameFile([i, USER_LABEL,XSS_STORED_LABEL, LEVEL_LABELS[3],PASS_FAIL_LABEL[1]])
        p = startPcap(XSS_STORED_FOLDER,PcapName)
        
    #Sql injection Low level attack
    XSS_STORED_ATTACK(browser, XSS_LEVEL[2])

    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)

XSS_CLEAR_BOOK(browser)








