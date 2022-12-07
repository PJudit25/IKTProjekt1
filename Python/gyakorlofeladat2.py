def feladat1():
    tomb = []
    for i in range(3):
        tomb.append(input("Kérek egy számot: "))
    #print(min(tomb))

    tomb.sort()
    print(tomb[0])
#feladat1()

def feladat2():
    tomb = []
    for i in range(3):
        tomb.append(input("Kérek egy számot: "))
    print(max(tomb))

    tomb.reverse()
    print(tomb[0])
#feladat2()

def feladat3():
    pontszam=int(input("Adja meg a pontszámot: "))

    if pontszam<50:
        print("Érdemjegy: 1")
    elif pontszam>=50 and pontszam<60:
        print("Érdemjegy: 2")
    elif pontszam>=60 and pontszam<70:
        print("Érdemjegy: 3")
    elif pontszam>=70 and pontszam<85:
        print("Érdemjegy: 4")
    else:
        print("Érdemjegy: 5")   

#feladat3()

def feladat4():
    szam=int(input("Kérem a számot: "))

    if szam%3==0 and szam%5==0:
        print("A szám osztható 3-al és 5-el.")
    if szam%3==0 and szam%5!=0:
        print("A szám osztható 3-al, de 5-el nem.")
    if szam%3!=0 and szam%5==0:
        print("A szám osztható 5-el, de 3-al nem.") 
    if szam%3!=0 and szam%5!=0:
        print("A szám nem osztható sem 3-al, sem 5-el.")               
#feladat4()

def feladat4b():
    oszthato = False

    szam=int(input("Kérek egy számot: "))
    if szam%3==0 or szam%5==0:
        oszthato=True
    print(oszthato)

#feladat4b()


def feladat5():
    tomb = []
    for i in range(3):
        tomb.append(int(input("Kérek egy számot: ")))
    if tomb[0]+tomb[1]==tomb[2] or tomb[1]+tomb[2]==tomb[0] or tomb[0]+tomb[2]==tomb[1]:
        print ("A számok közül kettő összege egyenlő a harmdik számmal :)")
    else:
        print("A megadott számok között nincs kettő olyan, melyek összege egyenlő lenne a harmadikkal :(")

#feladat5()

def feladat6():
    szam1=int(input("Kérem az első számot: "))
    szam2=int(input("Kérem a második számot: "))
    szam3=int(input("Kérem a harmadik számot: "))

    if szam1%2==0 and szam2%2==0 and szam3%2==0:
        print("Mindhárom szám páros.")
    else:
        print("A számok között van páratlan.")

#feladat6()

def feladat7():
    tomb=[]
    for i in range(2):
        tomb.append(input("Adjon meg egy szót: "))
    tomb.sort()
    print(tomb)

#feladat7()

def feladat8():
    tomb=[]
    szam=int(input("Adjon meg egy pozitív egész számot: "))
    eredetiszam=szam
    for i in range(3):
        if szam%3==0:
            while szam>0:
                tomb.append(szam)
                szam-=3
        else:
            szam-=1
    print(tomb)

#feladat8()

def feladat9():
    bekertSzam1=int(input("Adjon meg egy pozitív egész számot: "))
    bekertSzam2=int(input("Adjon meg egy pozitív egész számot: "))
    tomb=[]
    tomb.append(bekertSzam1)
    tomb.append(bekertSzam2)
    tomb.sort()
    print(tomb)
    szam1=tomb[0]
    szam2=tomb[1]-1
    tomb2=[]
    for i in range(2):
        if szam2%2==0:
            while szam2>szam1:
                tomb2.append(szam2)
                szam2-=2
        else:
            szam2-=1
    tomb2.sort()
    print(tomb2)

#feladat9()

def feladat10():
    szam=int(input("Adjon meg egy 20-nál nem nagyobb, pozitív egész számot: "))
    while szam>20:
        print("A megadott szám nagyobb, mint 20.")
        szam=int(input("Adjon meg egy 20-nál nem nagyobb, pozitív egész számot: "))
    print(szam*" "+"START")

feladat10()

    