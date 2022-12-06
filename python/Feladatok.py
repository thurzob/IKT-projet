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
import random
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
        
        
        
feladat4()