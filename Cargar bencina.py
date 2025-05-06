#Cargar bencina# 

num=int(input("Ingrese la cantidad de autos"))
for i in range(num):
    b=int(input("Cual bencina cargará: 1._93 - $800xlitro, 2._95 - $1000xlitro, 3._97 - $1500xlitro"))
    if b==1:
        print("Usted cargará bencima de 93")
        litros=int(input("¿Cuantos litros desea?"))
        total=litros*800
        print(f"Usted cargó {litros} litros de bencina de 93 y el total es {total}")
    elif b==2:
        print("Usted cargará bencima de 95")
        litros=int(input("¿Cuantos litros desea?"))
        total=litros*1000
        print(f"Usted cargó {litros} litros de bencina de 95 y el total es {total}")
    elif b==3:
        print("Usted cargará bencina de 97")
        litros=int(input("¿Cuantos litros desea?"))
        total=litros*1500
        print(f"Usted cargó {litros} litros de bencina de 97 y el total es {total}")
else:
        print("Error, seleccione una opción valida")

print(f"El total de ventas es: ", total)





   
