import random
n=random.randint(4,30)
k=0
while n>1:
    print("В куче",n,"камней")
    try:
        k=int(input("Игрок, введите число камней,которое вы хотели убрать(до трёх) "))
        while k<1 or k>3:
            print("Неверное число камней")
            k = int(input("Игрок, введите число камней,которое вы хотели убрать(до трёх) "))
    except:
        print("ТЫ ОШИБАЕШЬСЯ")
        exit()
    n=n-k
    if n==1:
        print("Вы победили!")
        break
    if n>4:
        k=random.randint(1,3)
    if n<=4:
        n=n-(n-1)
        print("Вы проиграли!")
        break
    n=n-k
    if n==1:
        print("Вы проиграли!")
        break
