"""0. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
a megadott szám értéke! """

def feladat0():
    szam=int(input("Adjon meg egy 20-nál nem nagyobb, pozitív egész számot: "))
    while szam>20:
        print("A megadott szám nagyobb, mint 20.")
        szam=int(input("Adjon meg egy 20-nál nem nagyobb, pozitív egész számot: "))
    print(szam*" "+"START")

#feladat0()


"""1. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
összege! """

def feladat1():
    szam=int(input("Adjon meg egy pozitív egész számot: "))
    tomb=[]
    for i in range(szam):
        tomb.append(szam)
        szam-=1
    print(tomb)
    print(sum(tomb))

#feladat1()       


"""2. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a
képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!""" 

def feladat2():
    szo=input("Kérek egy szót: ")
    for i in range(len(szo)):
        print(szo[i])

#feladat2()


"""3. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
pontosan a megadott szám legyen! """

def feladat3():
    szam=int(input("Adjon meg egy pozitív egész számot: "))
    szamjegyek="0 1 "
    if szam%2==0:
        print((szam//2)*szamjegyek)
    else:
        print((szam//2)*szamjegyek+"0")

#feladat3()


"""4. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
értékek között helyezkednek el! """

def feladat4():
    szam1=float(input("Adjon meg két valós számot! Kérem a kisebb számot: "))
    szam2=float(input("Kérem a nagyobb számot: "))
    szam1=int(szam1)
    szam2=int(szam2)
    tomb=[]
    kulonbseg=szam2-szam1
    for i in range(kulonbseg-1):
        tomb.append(int(szam1)+1)
        szam1+=1
    print(tomb)

#feladat4()


"""5. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre
a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!"""

def feladat5():
    N=int(input("Adjon meg egy pozitív egész számot: "))
    M=int(input("Adjon meg mégegy pozitív egész számot: "))
    for i in range(M):
        print(N*"*")

feladat5()

