import random
num_aleatorio=random.randint (1,10)
num=int(input("Ingrese un numero entre 1 y 10"))
while num!=num_aleatorio:
    num=int(input("Vuelva a ingresar un numero entre 1 y 10"))

print("Ese es el numero !")