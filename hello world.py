import random
import time as t
import string
import re
import datetime as dt

inputvar = int(input("welche aufg."))

rng = (random.randrange(3,40)) 


#Aufgabe 4
if(inputvar == 4):
    print(rng)
    counter = 3 
    while rng >= counter:
        div = counter / 3
        t.sleep(0.5)
        print(int(div))
        counter += 3

#Aufgabe 3
if(inputvar == 3):
    print(rng)
    if rng in range (3,40,3):
        print("alles fine")
    else:
        print("shi cooked")

#Aufgabe 5
if(inputvar==5):
    txt = str(input(""))
    liste = list(reversed(txt))
    liste1 = "".join(liste);
    print(liste1);

#Aufgabe 6
if(inputvar==6):
    txt1 = str(input(""))
    liste2 = list(reversed(txt1.lower()))
    liste3 = "".join(liste2);
    cap_rev = string.capwords(liste3)
    print(cap_rev)
    
#Aufgabe 7
if(inputvar==7):
    txt1 = str(input(""))
    liste2 = list(reversed(txt1.lower()))
    liste3 = "".join(liste2);
    cap_rev = string.capwords(liste3)
    no_spc = cap_rev.replace(" ", "")
    print(no_spc)

#Aufgabe 8
if(inputvar==8):
    #Havent fixed it yet due to me no understanding the question
    a = ("100+100")
    y = re.search("100", a)
    twinput = str(input(""))
    if y == twinput:
        print("twinnamon")
    else:
        print("we not twinnamon💔")

#Aufgabe 9
if(inputvar==9):
    #ohne regex
    c = int(input("Erste Zahl?"))
    b = int(input("Zweie Zahl?"))
    a = f"{c}+{b}={int(c) + int(b)}" 
    print(a)

if(inputvar==911):
    #mit regex
    c = input("Erste Zahl? ")  # z.B. "5"
    b = input("Zweite Zahl? ")  # z.B. "3"

    a = f"{c}+{b}"  # Erstellt den Text "5+3"
    yx = re.fullmatch(r"(\d+)\+(\d+)", a)

    if yx:
        # yx.group() liefert immer Text. int() macht Zahlen daraus.
        zahl1 = int(yx.group(1))
        zahl2 = int(yx.group(2))
    
        ergebnis = zahl1 + zahl2
        print(f"Das mathematische Ergebnis ist: {ergebnis}")

#Aufgabe.10
if(inputvar==10):
    dtnow = dt.datetime.now()
    dtweeklimit = dtnow.weekday() # Weekdays als Int (0 = Monday)
    dtrn = dtnow.time()
    strt = dt.time(7, 0, 0)
    end = dt.time(16, 30)

    if dtweeklimit < 5 and strt <= dtrn <= end:    
        c = int(input("Erste Zahl?"))
        b = int(input("Zweie Zahl?"))
        a = f"{c}+{b}={int(c) + int(b)}"
        print(a)
    else:
        print("nah lil chuddy")



