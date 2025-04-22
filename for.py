# num=9
# num=int(input("ingrese un numero"))
# for i in range(10):
#     print(num,"x",i+1,"=", (i+1)*num)

cant=int(input("Ingrese el numero de notas"))
for i in range(cant):
    print("Ingrese la nota"), i+1
    nota=float(input("Ingrese la nota", i))
    suma=suma+nota

prom=suma/cant    