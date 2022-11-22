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
    
    
feladat1()
