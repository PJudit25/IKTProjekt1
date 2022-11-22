import random

def feladat1():
    text=input("Jó napod van? ")

    if text=="Igen":
        print("Örülök neki.")
    elif text=="Nem":
        print("Nem örülök neki.")
    else:
        print("Sajnos nem értem a válaszodat!")

#feladat1()

def feladat2():
    number=int(input("Kérem a számot: "))

    if number%2==0:
        print("A szám páros.")
    else:
        print("A szám páratlan.")
        

#feladat2()

def feladat3():
    try:
        rnd=random.randrange(1,6)

        number=0
        while number<1 or number>5:
            number=int(input("Adj meg egy számot 1 és 5 között: "))

        if (number<rnd):
            print (f"A gép nagyobb számra gondolt: {rnd}")
        elif (number>rnd):
            print (f"A gép kisebb számra gondolt: {rnd}")
        else:
            print (f"Eltaláltad a gép által gondolt számot! {rnd}")
    except:
        print("Nem jó formátum.")

#feladat3()

def ciklus1():
    for i in range(1,11):
        if(i%2==0):
            print(i)

#ciklus1()

def ciklus2():
    for i in range(10,0,-1):
        print(i)

#ciklus2()

def ciklus3():
    for i in reversed(range(1,11)):
        if(i%2!=0):
            print(i)
ciklus3()