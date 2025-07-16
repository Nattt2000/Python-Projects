"""
text_corrector.py: zápočtový program, MFF UK
author: Natálie Zýková

Pro spuštění je potřeba mít stažený slovnik.txt ve stejném adresáři.
"""


# Libraries

import csv
import random as rd
import sys


# Functions

def levenstein(prvni,druhy):
    delkaprvni=len(prvni)
    delkadruhy=len(druhy)
    tabulka=[]
    for i in range(delkadruhy+1):
        a=[i]
        tabulka.append(a)
    for i in range(1,delkaprvni+1):
        tabulka[0].append(i)
    delka=0
    for i in range(1,delkadruhy+1):
        for j in range(1,delkaprvni+1):
            if prvni[j-1]==druhy[i-1]:
                delka=0
            else:
                delka=1
            prvek=min(delka+tabulka[i-1][j-1],tabulka[i-1][j]+1,tabulka[i][j-1]+1) 
            tabulka[i].append(prvek)
    return (tabulka[delkadruhy][delkaprvni])


def castechyby(kandidati, prvni, druhy):
    icka=["i","í","y","ý"]
    kratke=["a","e","o","u"]
    dlouhe=["á","é","ó","ú"]
    hacek=["ř","ž","š","č","ď","ť","ň","ě","ů"]
    bezhacek=["r","z","s","c","d","t","n","e","u"]
    znele=["b","v","d","g"]
    neznele=["p","f","t","k"]
    for i in range(len(kandidati)):
        if prvni[i] in icka and druhy[i] in icka:
            return kandidati[i]
        if (prvni[i]=="z" and druhy[i]=="s") or (prvni[i]=="s" and druhy[i]=="z"):
            return kandidati[i]
        if prvni[i] in kratke and druhy[i] in dlouhe:
            if kratke.index(prvni[i])==dlouhe.index(druhy[i]):
                return kandidati[i]
        if druhy[i] in kratke and prvni[i] in dlouhe:
            if kratke.index(druhy[i])==dlouhe.index(prvni[i]):
                return kandidati[i]
        if prvni[i] in hacek and druhy[i] in bezhacek:
            if hacek.index(prvni[i])==bezhacek.index(druhy[i]):
                return kandidati[i]
        if druhy[i] in hacek and prvni[i] in bezhacek:
            if hacek.index(druhy[i])==bezhacek.index(prvni[i]):
                return kandidati[i]
        if prvni[i] in znele and druhy[i] in neznele:
            if znele.index(prvni[i])==neznele.index(druhy[i]):
                return kandidati[i]
        if druhy[i] in neznele and prvni[i] in znele:
            if neznele.index(druhy[i])==znele.index(prvni[i]):
                return kandidati[i]
    return rd.choice(kandidati)
    

def vyber(slovo,seznam):
    kandi=[]
    zamenastary=[]
    zamenanovy=[]
    abeceda="aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyzž"
    for kandidat in seznam:
        if levenstein(slovo,kandidat)==0:
            return slovo
        if levenstein(slovo,kandidat)==1:
            for j in range(1,len(slovo)):
                for i in range(len(abeceda)):
                    novy=slovo[:j]+abeceda[i]+slovo[j+1:]
                    if novy in seznam:
                        zamenastary.append(slovo[j])
                        zamenanovy.append(abeceda[i])
                        kandi.append(novy) 
            if kandi==[]:
                return rd.choice(nej_slova)
            else:
                return castechyby(kandi,zamenastary,zamenanovy)
        else:
            return rd.choice(nej_slova)


# Others

slovnik=[]
zacatky = {}
pismeno = None
with open("slovnik.txt","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        slovo = row[0].lower()
        if not pismeno or slovo[0] != pismeno:
            pismeno = slovo[0]
            zacatky[pismeno] = i
        slovnik.append(slovo)
delka_slovniku = i+1

text=[x for x in input().split()]
for vstup in text:
    nej_hodnota = float("inf")
    zac = zacatky[vstup[0]]
    nej_slova = []
    for i in range(zac, delka_slovniku): 
        if vstup[0] != slovnik[i][0]:
            break
        delka = levenstein(vstup[1:], slovnik[i][1:])
        if delka < nej_hodnota:
            nej_hodnota = delka
            nej_slova = [slovnik[i]]
        elif delka == nej_hodnota:
            nej_slova.append(slovnik[i])
    print(vyber(vstup,nej_slova), end=" ")
    print(nej_slova)








