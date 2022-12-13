#0. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
#felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
#a megadott szám értéke!

def feladat0():
    Szam=int(input("Adj meg egy számot ami 20-nál kissebb! "))
    if(Szam<=20):
        print(" "*Szam, "START")
        
#feladat0()

#1. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
#összege! 

def feladat1():
    tomb=[]
    Szam=int(input("Adj meg egy poiztív egész számot! "))
    for i in range(Szam+1):
        tomb.append(i)
        print(i)
    osszeg=sum(tomb)
    print(osszeg)
        
        

   
feladat1()

#2. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a
#képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!

def feladat2():
    Szo=input("Adj meg egy szót! ")
    for i in str(Szo):
        print(i)
        
#feladat2()

#3. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
#pontosan a megadott szám legyen! 

def feladat3():
    Szam=int(input("Adj meg egy pozitív egész számot! "))
    for i in range(Szam):
        if i%2==0:
            print("0", end=" ")
        else:
            print("1", end=" ")


#feladat3()

#4. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
#számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
#értékek között helyezkednek el! 

def feladat3():
    Szam1=int(input("Adj meg egy nagyobb pozitív egész számot! "))
    Szam2=int(input("Adj meg egy kissebb pozitív egész számot! "))
    for i in range(Szam2+1,Szam1):
        print(i)
    
#feladat3()

#5. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre
#a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
#téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!

def feladat4():
    N=int(input("Kérem az N paramétert! "))
    M=int(input("Kérem az M paramétert! "))
    for i in range(N):
        print("*"*M)
        
#feladat4()