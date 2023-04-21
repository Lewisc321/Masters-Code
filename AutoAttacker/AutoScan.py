# -*- coding: utf-8 -*-
"""
Created on Sun Jan  15 16:02:30 2023

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
time.sleep(1)

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SCAN_FOLDER)
    
for i in range(1,EASY_PASS+1):
    #Click SQLI link 
    clickLink_XPATH(browser, HOME_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SCAN_LABEL])
        else:
            PcapName = nameFile([i, USER_LABEL,SCAN_LABEL])
        p = startPcap(SCAN_FOLDER,PcapName)
        
    #Sql injection Low level attack
    QUICKSCAN(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SCAN_FOLDER)
    
for i in range(1,MED_PASS+1):
    #Click SQLI link 
    clickLink_XPATH(browser, HOME_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SCAN_LABEL])
        else:
            PcapName = nameFile([i, USER_LABEL,SCAN_LABEL])
        p = startPcap(SCAN_FOLDER,PcapName)
        
    #Sql injection Low level attack
    QUICKSCAN(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SCAN_FOLDER)
    
for i in range(1,HARD_PASS+1):
    #Click SQLI link 
    clickLink_XPATH(browser, HOME_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SCAN_LABEL])
        else:
            PcapName = nameFile([i, USER_LABEL,SCAN_LABEL])
        p = startPcap(SCAN_FOLDER,PcapName)
        
    #Sql injection Low level attack
    QUICKSCAN(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)

if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SCAN_FOLDER)
for i in range(1,MED_FAIL+1):
    #Click SQLI link 
    clickLink_XPATH(browser, HOME_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SCAN_LABEL])
        else:
            PcapName = nameFile([i, USER_LABEL,SCAN_LABEL])
        p = startPcap(SCAN_FOLDER,PcapName)
        
    #Sql injection Low level attack
    QUICKSCAN(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SCAN_FOLDER)
    
for i in range(1,HARD_FAIL+1):
    #Click SQLI link 
    clickLink_XPATH(browser, HOME_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SCAN_LABEL])
        else:
            PcapName = nameFile([i, USER_LABEL,SCAN_LABEL])
        p = startPcap(SCAN_FOLDER,PcapName)
        
    #Sql injection Low level attack
    QUICKSCAN(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)


if ABSOLUTE_NUMBERING:
    currentNumb = getAbsoluteNumber(SCAN_FOLDER)
    
for i in range(1,IMPOSS_FAIL+1):
    #Click SQLI link 
    clickLink_XPATH(browser, HOME_XPATH)
    #If using VM start PCAP
    if USING_VM :
        if ABSOLUTE_NUMBERING:
            PcapName = nameFile([currentNumb + i, USER_LABEL,SCAN_LABEL])
        else:
            PcapName = nameFile([i, USER_LABEL,SCAN_LABEL])
        p = startPcap(SCAN_FOLDER,PcapName)
        
    #Sql injection Low level attack
    QUICKSCAN(browser)
    
    #If using VM start PCAP
    if USING_VM :
        endPcap(p)
