def optiunea1():
    print("-> Ai ales Opțiunea 1! Codul pornește...\n")

def optiunea2():
    print("-> Ai ales Opțiunea 2! Codul pornește...\n")

def optiunea3():
    print("-> Ai ales Opțiunea 3! Codul pornește...\n")

while True:
    print("=== MENIU PRINCIPAL ===")
    print("1 - Porneste Opțiunea 1")
    print("2 - Porneste Opțiunea 2")
    print("3 - Porneste Opțiunea 3")
    print("0 - Ieșire din program")
    
    optiune = input("Alege o opțiune: ")
    
    if optiune == "1":
        optiunea1()
    elif optiune == "2":
        optiunea2()
    elif optiune == "3":
        optiunea3()
    elif optiune == "0":
        print("La revedere! Programul s-a încheiat.")
        break  # Oprim bucla while
    else:
        print("Opțiune greșită! Încearcă din nou.\n")