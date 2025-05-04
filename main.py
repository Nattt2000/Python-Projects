"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Natálie Zýková
email: natalie.zykova@seznam.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

import string

slovnik_registrovanych = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

username = "bob"
password = "123"
cislo_textu = 1

if slovnik_registrovanych.get(username) == password:
    print(f"username: {username} \npassword: {password}")
    print("----------------------------------------")
    print(f"Welcome to the app, {username}. \nWe have 3 texts to be analyzed.")
    print("----------------------------------------")
    print(f"Enter a number btw. 1 and 3 to select: {cislo_textu}")
    print("----------------------------------------")
    
    if not cislo_textu in range(4):
        print("wrong number, terminating the program..")
    else:
        vybrany_text = TEXTS[cislo_textu - 1]
        soucet_slov = len(vybrany_text.split())
        print(f"There are {soucet_slov} words in the selected text.")
        
        soucet_title = 0
        for slovo in vybrany_text.split():
            if slovo.istitle():
                soucet_title += 1
        print(f"There are {soucet_title} titlecase words.")

        soucet_upper = 0
        for slovo in vybrany_text.split():
            if slovo.isupper():
                soucet_upper += 1
        print(f"There are {soucet_upper} uppercase words.")

        soucet_lower = 0
        for slovo in vybrany_text.split():
            if slovo.islower():
                soucet_lower += 1
        print(f"There are {soucet_lower} lowercase words.")

        pocet_cisel = 0
        for znak in vybrany_text.split():
            if znak.isdigit():
                znak = znak.strip(string.punctuation)
                pocet_cisel += 1
        print(f"There are {pocet_cisel} numeric strings.")

        soucet_cisel = 0
        for znak in vybrany_text.split():
            if znak.isdigit():
                znak = znak.strip(string.punctuation)
                soucet_cisel += int(znak)
        print(f"The sum of all the numbers {soucet_cisel}")
        print("----------------------------------------")

        print("LEN|  OCCURENCES  |NR.")
        print("----------------------------------------")
        

        pocty = []
        for i in range(1, 15):
            ipismena_slova = []
            for slovo in vybrany_text.split():
                slovo_bez = slovo.strip(string.punctuation)
                if len(slovo_bez) == i:
                    ipismena_slova.append(slovo_bez)
            pocet_slov = len(ipismena_slova)
            pocty.append(pocet_slov)
        maximum = max(pocty)


        for index in range(len(pocty)):
            if pocty[index] == 0:
                continue
            else:
                if index < 9:
                    mod_index = f" {index + 1}"
                else:
                    mod_index = index + 1
                pocet_hvezdicek = "*" * pocty[index]
                koef = maximum - pocty[index]
                pocet_mezer = " " * koef
            print(mod_index, "|", pocet_hvezdicek, pocet_mezer, "|", pocty[index])


else:
   print("unregistered user, terminating the program..")
