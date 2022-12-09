# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:49:19 2022

@author: Callum Manning

Strath Uni - 201720173
"""
#My Modules
from ExtModulesSetUp import *


def quotedCommaParser(line):
    line= line.split(';')[0]
    lineArray = line.split(',');
    QuoteCheck = False;
    part1 =''
    outputArray = []
    for section in lineArray:
        if '"' in section:
            if QuoteCheck == True:
                outputArray.append((part1 + ',' + section).replace('"', ''))
                QuoteCheck = False;
                part1 =''
            else:
                QuoteCheck = True
                part1 = section;
        else:
            outputArray.append(section)
            QuoteCheck = False;
            part1 =''
    return outputArray



def sqliStatementGenerator(needApostraphe):
    i = 0;
    with open("poss_SQLI_Injections.csv") as file_in:
        array = []
        for line in file_in:
            if i == 3:
                row = quotedCommaParser(line)
            else:
                row = line.split(';')[0].split(',')
            array.append(row)
            i = i + 1
    nonesense = random.choice(array[0])
    operator =  ' ' + random.choice(array[1]) + ' '
    equals = random.choice(array[2]) + ' '
    statement = random.choice(array[3]) + ' '
    comment = random.choice(array[4])
    
    if needApostraphe:
        statement = nonesense + "'" + operator + equals + statement + comment
    else:
        statement = nonesense + operator + equals + statement + comment
    return statement


def comiStatementGenerator(level):
    i = 0;
    with open("poss_COMS_Injections.csv") as file_in:
        array = []
        for line in file_in:
            row = line.split(';')[0].split(',')
            array.append(row)
            i = i + 1
    nonesense = random.choice(array[0])
    
    if level == 1:
        operator = random.choice(array[1])
    elif level == 2:
        operator = random.choice(array[2])
    elif level == 3:
        operator = random.choice(array[3])
    
    command = random.choice(array[4])
    
    statement = nonesense + operator + command
    return statement



