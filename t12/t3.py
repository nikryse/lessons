def robot_hello():
    spisok = ["Timur","Evgeniy","Alexey","Sergey"]
    ima = input("Введите имя: ")
    if ima not in spisok:
        print(f"Привет {ima},вас нет в списке. Рад знакомству!")
        spisok.append(ima)
    else:
        print(f"Привет,{ima}!")
robot_hello()