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

    if number%2==0:
        print("a Szám páros szám")
    elif number%2>0:
        print("A szám páratlan")
    else:
        print(f"Nem jó értéket adtál meg.")
       

feladat2()