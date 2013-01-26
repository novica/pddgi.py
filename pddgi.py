#!/usr/bin/env python2
# -*- coding: utf-8 -*-


#Скрипта што генерира правилен ПДД-ГИ излез по внесување на податоци
#за секое лице што примило средства.

#Треба да се генерираат две .TXT датотеки.

#import string


spisok = open('vraboteni.txt', 'r')
gipoed = open('GI_POED.TXT', 'w')
gisumar = open('GI_SUMAR.TXT', 'a') #Претпоставка дека во GI_SUMAR.TXT веќе се запишани генералиите на компанијата

#Претпоставка дека списокот е составен од матичен број и
#име и презиме поделени со запирка

suma = {'bruto12': '','odbitoci12': '', 'olesnuvanje10': '', 'pdd12': '', 'neto12': ''}


prompt = 'Внеси шифра за вид на примања (мора да биде 2 знаци):\n'
    code2 = raw_input(prompt)
    if isinstance(code2, int):
        code2 = str(code2)

broj5 = 0

for line in spisok:
    broj5 = broj5 + 1
    #Постави dictionary. Бројките означуваа колку знаци смее да биде
    #долга секоја ставка.
    vraboten = {'embg13': '', 'ime40': '', 'bruto10': '',
        'odbitoci10': '', 'olesnuvanje7': '', 'pdd10': '', 'neto10': ''}
    line = line.split(',')
    vraboten['embg13'] = line[0]
    line[1]  = line[1].strip()
    while len(line[1]) < 40:
        line[1] = line[1] + ' '
    vraboten['ime40'] = line[1]
    #Сега побарај податоци:

    prompt = 'Внеси бруто примања за ' + vraboten['ime40'].strip() + ':\n'
    vraboten['bruto10'] = raw_input(prompt)
    suma['bruto12'] = suma['bruto12'] + vraboten['bruto10']
    vraboten['bruto10'] = str(vraboten['bruto10'])
    while len(vraboten['bruto10']) < 10:
        vraboten['bruto10'] = "0" + vraboten['bruto10']

    prompt = 'Внеси одбитоци за ' + vraboten['ime40'].strip() + ':\n'
    vraboten['odbitoci10'] = raw_input(prompt)
    suma['odbitoci12'] = suma['odbitoci12'] + vraboten['odbitoci10']
    vraboten['odbitoci10'] = str(vraboten['odbitoci10'])
    while len(vraboten['odbitoci10']) < 10:
        vraboten['odbitoci10'] = "0" + vraboten['odbitoci10']

    prompt = 'Внеси даночно олеснување за ' + vraboten['ime40'].strip() + ':\n'
    vraboten['olesnuvanje7'] = raw_input(prompt)
    suma['olesnuvanje10'] = suma['olesnuvanje10'] + vraboten['olesnuvanje7']
    vraboten['olesnuvanje7'] = str(vraboten['olesnuvanje7'])
    while len(vraboten['olesnuvanje7']) < 7:
        vraboten['olesnuvanje7'] = "0" + vraboten['olesnuvanje7']

    prompt = 'Внеси ПДД за ' + vraboten['ime40'].strip() + ':\n'
    vraboten['pdd10'] = raw_input(prompt)
    suma['pdd12'] = suma['pdd12'] + vraboten['pdd10']
    vraboten['pdd10'] = str(vraboten['pdd10'])
    while len(vraboten['pdd10']) < 10:
        vraboten['pdd10'] = "0" + vraboten['pdd10']

    prompt = 'Внеси нето примања за ' + vraboten['ime40'].strip() + ':\n'
    vraboten['neto10'] = raw_input(prompt)
    suma['neto12'] = suma['neto12'] + vraboten['neto10']
    vraboten['neto10'] = str(vraboten['neto10'])
    while len(vraboten['neto10']) < 10:
        vraboten['neto10'] = "0" + vraboten['neto10']

    pddgiline = code2 + vraboten['embg13'] + vraboten['ime40']+ vraboten['bruto10'] + vraboten['odbitoci10'] + vraboten['olesnuvanje7'] + vraboten['pdd10'] + vraboten['neto10'] + '\n'
    
    gipoed.write(pddgiline)
    

for val in suma.values():
   val=str(val)

while len(suma['bruto12'] < 12:
    suma['bruto12'] = '0' +  suma['bruto12']

while len(suma['odbitoci12'] < 12:
    suma['odbitoci12']] = '0' +  suma['odbitoci12']

while len(suma['odbitoci12'] < 10:
    suma['odbitoci12'] = '0' +  suma['odbitoci12']

while len(suma['pdd12'] < 12:
    suma['pdd12'] = '0' +  suma['pdd12']

while len(suma['neto12'] < 12:
    suma['neto12'] = '0' +  suma['neto12']

broj5 = str(broj5)

while len(broj5) < 5
    broj5 = '0' +  broj5

sumarline = code2 + broj5 + suma['bruto12'] + suma['odbitoci12'] + suma['olesnuvanje10'] + suma['pdd12'] + suma['neto12']
gisumar.append(sumarline)

spisok.close()
gipoed.close()
gisumar.close()