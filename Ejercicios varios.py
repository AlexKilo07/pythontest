# 1) Pida al usuario un numero y clasifiquelo como par o impar
# muestre los pares e impares del 1 hasta ese numero

# 2) Pida al usuario ingresar numero, al final debe mostrar cuantos numeros se ingresaron y mostrar la suma de todos ellos
# para terminar, debe poner la palabra salir

# 3) Pida al usuario ingresar un numero y multiplicalo por un numero al azar entre 2 y 8. Si el numero es mayyor que 50
# logró la meta, si no, intente nuevamente

# 4) Ingresar un numero positivo, multiplicarlo por 5, restarle 8, sumarle 3 y dividirlo por 2

# 1)
num=int(input("Ingrese un numero"))
if (num % 2==0):
    print("Es par")
else:
    print("Es impar")

print("Los numeros pares entre 1 y (num) son: ") 
for i in range(1,num+1):
    if(i%2==0):
 