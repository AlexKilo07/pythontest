# import time
# num=10
# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp="no"

# while resp!="si":
#     resp=input("desea salir del sistena?")

clave=3344

contraseña=int(input("Ingrese contraseña"))

while clave!=contraseña:
    print("ERROR, clave invalida")
    contraseña=int(input("Ingrese contraseña"))
print ("Clave aceptada")