# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 03:25:14 2022

@author: Callum Manning

Strath Uni - 201720173


"""

import time


def readPassList():
    with open("most_common_passwords_2.txt") as file_in:
        PassDic= {};
        i = 0;
        for line in file_in:
            if line != '\n':
                PassDic[i]=line.replace('\n','');
                i = i+1;
        return PassDic

def PassCracker(passHashNo, PassDic):
    return PassDic[passHashNo]



PassDic = readPassList();
