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

username = input("username: ")
password = input("password: ")
pocet_textu = len(TEXTS)
oddelovac = "----------------------------------------"

if slovnik_registrovanych.get(username) == password:
    print(oddelovac)
    print(f"Welcome to the app, {username}. \nWe have {pocet_textu} texts to be analyzed.")
    print(oddelovac)
    
    
    try:
        cislo_textu = int(input(f"Enter a number btw. 1 and {pocet_textu} to select: "))
    except ValueError:
        print("wrong number, terminating the program..")
    else:
        if not cislo_textu in range(1, pocet_textu + 1):
            print("wrong number, terminating the program..")
        else:
            print(oddelovac)
            vybrany_text = TEXTS[cislo_textu - 1]
            soucet_slov = len(vybrany_text.split())
            print(f"There are {soucet_slov} words in the selected text.")
            
            soucet_title = 0
            soucet_upper = 0
            soucet_lower = 0
            pocet_cisel = 0
            soucet_cisel = 0
            
            for znak in vybrany_text.split():
                if znak.istitle():
                    soucet_title += 1
                
                if znak.isupper():
                    soucet_upper += 1

                if znak.islower():
                    soucet_lower += 1

                if znak.isdigit():
                    znak = znak.strip(string.punctuation)
                    pocet_cisel += 1
                    soucet_cisel += int(znak)      

            print(f"There are {soucet_title} titlecase words.")
            print(f"There are {soucet_upper} uppercase words.")
            print(f"There are {soucet_lower} lowercase words.")
            print(f"There are {pocet_cisel} numeric strings.")
            print(f"The sum of all the numbers {soucet_cisel}")
            
            print(oddelovac)

            print("LEN|  OCCURENCES  |NR.")
            print(oddelovac)

            cetnosti = dict()
            for slovo in vybrany_text.split():
                slovo_bez = slovo.strip(string.punctuation)
                delka_slova = len(slovo_bez)
                if delka_slova in cetnosti:
                    cetnosti[delka_slova] += 1
                else:
                    cetnosti[delka_slova] = 1
            
            maximum = max(cetnosti.values())
            for klic, hodnota in sorted(cetnosti.items()):
                pocet_hvezdicek = "*" * hodnota
                print(f"{klic:>2}|{pocet_hvezdicek:<{maximum + 5}}|{hodnota}")

else:
   print("unregistered user, terminating the program..")
