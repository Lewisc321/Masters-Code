# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:11:44 2022

@author: Callum Manning

Strath Uni - 201720173
"""


#My Modules
from UserSetUp import *
from ExtModulesSetUp import *

def nameFile(NameTexts):
    i = 0;
    output = '';
    for text in NameTexts:
        text = str(text)
        if i == (len(NameTexts)):
            output = output + text
        output = output + text + '_'
        i = i + 1;
    return output +'.pcap'
        


def getAbsoluteNumber(folder):
    if os.path.isdir(folder):
        return len(os.listdir(folder))
    else:
        return False
    

