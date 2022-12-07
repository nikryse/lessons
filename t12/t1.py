def calcul():
    chis1  = int(input("Введите 1 число: "))
    znak = input("Введите знак: ")
    chis2 = int(input("Введите 2 число: "))
    if znak == "+":
        print(chis1 + chis2)
    elif znak == "-":
        print(chis1-chis2)
    elif znak == "/" and chis2 != 0:
        print(chis1 / chis2)
    elif znak == "*":
        print(chis1*chis2)
    else:
        print("Ошибка")
calcul()