#!/usr/bin/env python2
# -*- coding: utf-8 -*-


#Скрипта што генерира правилен ПДД-ГИ излез по внесување на податоци
#за секое лице што примило средства.

#Треба да се генерираат две .TXT датотеки.

#import string


spisok = open('vraboteni.txt', 'r')
gipoed = open('GI_POED.txt', 'w')

#Претпоставка дека списокот е составен од матичен број и
#име и презиме поделени со запирка

for line in spisok:
    #Постави dictionary. Бројките означуваа колку знаци смее да биде
    #долга секоја ставка.
    vraboten = {'code2': '', 'embg13': '', 'ime40': '', 'bruto10': '',
        'odbitoci10': '', 'olesnuvanje7': '', 'pdd10': '', 'neto10': ''}
    line = line.split(',')
    vraboten['embg13'] = line[0].rstrip('\n')
    while len(line[1]) < 40:
        line[1] = line[1] + ' '
    vraboten['ime40'] = line[1].rstrip('\n')
    #Сега побарај податоци:
    
    prompt = 'Внеси шифра на примања за' + vraboten['ime40'] + ':\n' 
    vraboten['code2'] = raw_input(prompt)
    #if  vraboten['code2'] е број???:
    #    vraboten['code2'] = str(vraboten['code2'])
    
    
    prompt = 'Внеси бруто примања за' + vraboten['ime40'] + ':\n' 
    vraboten['bruto10'] = raw_input(prompt)
    vraboten['bruto10'] = str(vraboten['bruto10'])
    while len(vraboten['bruto10']) < 10:
        vraboten['bruto10'] = "0" + vraboten['bruto10']
    
    prompt = 'Внеси одбитоци за' + vraboten['ime40'] + ':\n' 
    vraboten['odbitoci10'] = raw_input(prompt)
    vraboten['odbitoci10'] = str(vraboten['odbitoci10'])
    while len(vraboten['odbitoci10']) < 10:
        vraboten['odbitoci10'] = "0" + vraboten['odbitoci10']
    
    prompt = 'Внеси даночно олеснување за' + vraboten['ime40'] + ':\n' 
    vraboten['olesnuvanje7'] = raw_input(prompt)
    vraboten['olesnuvanje7'] = str(vraboten['olesnuvanje7'])
    while len(vraboten['olesnuvanje7']) < 7:
        vraboten['olesnuvanje7'] = "0" + vraboten['olesnuvanje7']
    
    prompt = 'Внеси ПДД за' + vraboten['ime40'] + ':\n' 
    vraboten['pdd10'] = raw_input(prompt)
    vraboten['pdd10'] = str(vraboten['pdd10'])
    while len(vraboten['pdd10']) < 10:
        vraboten['pdd10'] = "0" + vraboten['pdd10']
    
    prompt = 'Внеси нето примања за' + vraboten['ime40'] + ':\n' 
    vraboten['neto10'] = raw_input(prompt)
    vraboten['neto10'] = str(vraboten['neto10'])
    while len(vraboten['neto10']) < 10:
        vraboten['neto10'] = "0" + vraboten['neto10']
    
    
    
    pddgiline = vraboten['code2']+ vraboten['embg13'] + vraboten['ime40']+ vraboten['bruto10'] + vraboten['odbitoci10'] + vraboten['olesnuvanje7'] + vraboten['pdd10'] + vraboten['neto10'] + '\n'
    
    gipoed.write(pddgiline)
    
spisok.close()
gipoed.close()
