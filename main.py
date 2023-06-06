def pr1():
    n = input('Введите кол-во слов: ')
    b = input('Введи слово:')
    l1 = b
    for i in range(int(n)-1):
        a = input('Введите слово:')
        l1 = l1 + ' ' + a
    print(l1)



def pr2():
    l1 = []
    b = ''
    while b != 'stop':
        b = input('Введи слово:')
        l1.append(b)
    for i in l1:
        print(i, end=" ")

pr2()
def pr3():
    slovo = input("Введите слово: ")
    for i in range(len(slovo)):
        if slovo[i] == "ф" or slovo[i] == "Ф":
            print("Ого! Это редкое слово!")
            break
        else:
            print("Эх, это не очень редкое слово...")
            break


def pr4():
    from random import randint

    k = 0
    prav = "Правильный ответ"
    neprav = "Неправильный ответ"

    a = ""
    while not a == "stop":
        chislo = randint(0, 10)
        chislo2 = randint(0, 10)
        a = input(str(chislo) + "+" + str(chislo2) + "=")
        b = int(chislo) + int(chislo2)
        if a == "stop":
            break
        else:
            if int(a) == b:
                print(prav)
            else:
                print(neprav)
                k +=1
                if k == 3:
                    print("3 неправильных ответа")
                    break


