#Kérj be 3 számot és írasd ki a legkissebbet. (Min Függvény)
import random
def feladat1():
    Szam=[]
    for i in range(3):
        Szam.append(int(input("Kérek egy számot! ")))
    
    print(min(Szam))

#feladat1()

#Kérj be 3 számot és írasd ki a legnagyobbat. (Max Függvény)
def feladat2():
    Szam=[]
    for i in range(3):
        Szam.append(int(input("Kérek egy számot! ")))
    
    print(max(Szam))

#feladat2()

#Add meg a dolgozat pontszámát majd írj programot ami kiadja a pontszámnak megfelelő jegyet!
def feladat3():
    pontSzam=int(input("Kérem a dolgozat pontszámát! "))
    if(pontSzam<50):
        print(1)
    if(50<=pontSzam<60):
        print(2)
    if(60<=pontSzam<70):
        print(3)
    if(70<=pontSzam<85):
        print(4)
    if(pontSzam>85):
        print(5)

#feladat3()

#Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
#hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!
def feladat4():
    szam=int(input("Adjon meg egy számot! "))
    if(szam%3==0 and szam%5==0):
        print("Osztható 3-mal és 5-tel.")
    elif(szam%3!=0 and szam%5!=0):
        print("Nem osztható 3-mal és 5-tel sem.")
    elif(szam%3==0 and szam%5!=0):
        print("csak 3-mal osztható")
    elif(szam%3!=0 and szam%5==0):
        print("Csak 5-tel osztható")

             
#feladat4()

#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
#hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!
def feladat5():
    szam1=int(input("Add meg az első számot! "))
    szam2=int(input("Add meg a második számot! "))
    szam3=int(input("Add meg a harmadik számot! "))
    if(szam1+szam2==szam3):
        print("Az első és második szám összege egyenlő a harmadik számmal.")
    elif(szam1+szam3==szam2):
        print("Az első és harmadik szám összege egyenlő a második számmal.")
    elif(szam2+szam3==szam1):
        print("A második és harmadik szám összege egyenlő az első számmal")
    else:
        print("nincs két szám amelynek összege egyenlő lenne a harmadikkal")
        
    

#feladat5()

#Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a
#képernyőre, hogy mind a három páros szám-e (igen/nem)!

def feladat6():
    tomb=[]
    for szam in range(3):
        szam=int(input("Adjon meg egy számot! "))
        tomb.append(szam)
    print(tomb)
    for i in tomb:
        if(i%2!=0):
            print("Nem páros")
        else:
            print("Páros") 
#feladat6()

#Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben
#kiírja őket a képernyőre!
def feladat7():
    szavak=[]
    for szo in range(2):
        szo=input("Kérek egy szót! ")
        szavak.append(szo)
    szavak.sort()
    print(szavak)


feladat7()