import asyncio
import random

from time import sleep


async def say_after(delay, wait):
    await asyncio.sleep(delay)
    print(wait)


async def main():
    numeroBolinhas = [1,2, 3, 4, 5, 6, 7, 8, 9]
    bolinhas = [1, 1, 1, 1, 1, 1, 1, 1, 2]

    random.shuffle(bolinhas)
    print("Misturando as bolinhas...")
    await say_after(2, "Bolinhas misturadas!\n")

    sleep(2)

    print("Nome das bolinhas: " + str(numeroBolinhas))
    print("Peso das bolinhas: " + str(bolinhas) + "\n")

    grupoA = [bolinhas[0], bolinhas[1], bolinhas[2]]
    grupoB = [bolinhas[3], bolinhas[4], bolinhas[5]]
    grupoC = [bolinhas[6], bolinhas[7], bolinhas[8]]

    sleep(2)

    print("Grupo A: {}".format(grupoA))
    print("Grupo B: {}".format(grupoB))
    print("Grupo C: {}".format(grupoC) + "\n")

    print("Pesando as bolinhas...\n")

    sleep(2)

    balanca(grupoA, grupoB, grupoC, bolinhas)


def balanca(grupoA, grupoB, grupoC, bolinhas):
    somaA = sum(grupoA)
    somaB = sum(grupoB)
    somaC = sum(grupoC)

    if somaA == somaB:
        print("Resultado da primeira pesagem:\nos grupos A e B tem o mesmo peso.")
        print("O grupo C é o mais pesado!\n")
        sleep(2)

        if bolinhas[6] == bolinhas[7]:
            print("Resultado da segunda pesagem:\nas bolinhas 7 e 8 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 9 = " + str(bolinhas[8]))
            sleep(2)
            exit()
        elif bolinhas[6] == bolinhas[8]:
            print("Resultado da segunda pesagem:\nas bolinhas 7 e 9 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 8 = " + str(bolinhas[7]))
            sleep(2)
            exit()
        else:
            print("Resultado da segunda pesagem:\nas bolinhas 8 e 9 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 7 = " + str(bolinhas[6]))
            sleep(2)
            exit()

    elif somaA == somaC:
        print("Resultado da primeira pesagem:\nos grupos A e C tem o mesmo peso.")
        print("O grupo B é o mais pesado!\n")

        if bolinhas[3] == bolinhas[4]:
            print("Resultado da segunda pesagem:\nas bolinhas 4 e 5 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 6 = " + str(bolinhas[5]))
            sleep(2)
            exit()
        elif bolinhas[3] == bolinhas[5]:
            print("Resultado da segunda pesagem:\nas bolinhas 4 e 6 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 5 = " + str(bolinhas[4]))
            sleep(2)
            exit()
        else:
            print("Resultado da segunda pesagem:\nas bolinhas 5 e 6 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 4 = " + str(bolinhas[3]))
            sleep(2)
            exit()

    else:
        print("Resultado da primeira pesagem:\nos grupos B e C tem o mesmo peso.")
        print("O grupo A é o mais pesado!\n")

        if bolinhas[0] == bolinhas[1]:
            print("Resultado da segunda pesagem:\nas bolinhas 1 e 2 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 3 = " + str(bolinhas[2]))
            sleep(2)
            exit()
        elif bolinhas[0] == bolinhas[2]:
            print("Resultado da segunda pesagem:\nas bolinhas 1 e 3 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 2 = " + str(bolinhas[1]))
            sleep(2)
            exit()
        else:
            print("Resultado da segunda pesagem:\nas bolinhas 2 e 3 tem o mesmo peso.")
            print("A bolinha mais pesada é a bolinha 1 = " + str(bolinhas[0]))
            sleep(2)
            exit()


if __name__ == "__main__":
    asyncio.run(main())
