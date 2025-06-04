cant=int(input("Cantidad de niños"))
for i in range (cant):
    huevos=int(input("Cuantos huevos encontro?"))
    if huevos<12:
        print("Es un noob")
    elif huevos>=12 and huevos<=24:
        print("Es un master")
    elif huevos>=25:
        print("Es una leyenda")
    else:
        print("Ingrese un numero valido")
        

