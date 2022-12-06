#1.1 Feladat
#Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
def feladat1():
    Day=input("Üdv, jó napja van? ")
    if Day=="igen":
        print("Örülök neki! ")
    elif Day=="nincs":
        print("Nem örülök neki. ")
    else:
        print("Ilyen válasz nincs, az előre megírt programban.")
    
    
#feladat1()


#2. Feladat
#Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!
def feladat2():
 
    number=int(input("Kérem a számot! "))

    pass
    if number%2==0:
        print("a Szám páros szám")
    elif number%2>0:
        print("A szám páratlan")
    else:
        print("Nem jó értéket adtál meg.")
    

#feladat2()
#3. Feladat
#Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
#-----------------------------------------------------------------------------------------------------------------------------------------
import random

def osszehasonlitas(veletlenSzam, megadottSzam):
    try:
        megadottSzam=int(megadottSzam)
        if(veletlenSzam>megadottSzam):
            return(f"A gép nagyobb számra gondolt: {veletlenSzam}")
        elif(megadottSzam>veletlenSzam):
            return(f"A gép kissebb számra gonolt: {veletlenSzam}")
        else:
            return(f"Eltaláltad a gép által gondolt számot", {veletlenSzam})
    except:
        return"Nem számot adtál meg..." 
    
        

#veletlenSzam=random.randrange(1,17)
#megadottSzam=(input("Adj meg egy számot!"))
#uzenet=osszehasonlitas(veletlenSzam,megadottSzam)
#print(uzenet)
#----------------------------------------------------------------------------------------------
#1. Feladat
#Írj egy programot, amely kiírja a páros számokat 1 és 10 között!
def ciklus():
    for i in range(1,11):
        if i%2==0:
            print (i)
        
#ciklus()
#----------------------------------------------------------
#Páratlan számok csökkenő sorrendben.
def ciklus2():
    for i in reversed(range(1,10,)):
        if i%2!=0:
            print(i)

#ciklus2()
#--------------------------------------------------------
def ciklus3():
    number=int(input("Kérem az ismétlések számát! "))
    text=input("Kérem az ismétlendő szöveget! ")
    for i in range(number):
        print(text)

#ciklus3()
#-------------------------------------------------------------
def ciklus4():
    number=1
    while number%2!=0:
        number=int(input("Kérek egy számot! "))

#ciklus4()
#--------------------------------------------------------------
def ciklus5():
    print("Ezek a 3-mal osztható számok:")
    db=int(0)
    for i in range(20):
        rnd=random.randrange(1,13)
        if rnd%3==0:
            print(rnd)
            db=db+1
    
    
ciklus5()   