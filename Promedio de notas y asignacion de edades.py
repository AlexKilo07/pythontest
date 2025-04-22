# Determinar el promedio de 3 numeros

# print ("Ingrese 3 numeros")
# n1=int(input())
# n2=int(input())
# n3=int(input())
# prom=(n1+n2+n3)/3
# print("Su promedio es", prom)

# if prom<40:
#    print("Usted reprobó")
# else:
#      print("Usted aprobó")

# Calificar las personas según su edad
# Menor de 12 es niño
# Entre 12 y 17 adolescente
# Entre 18 y 64 adulto
# 65 y mas adulto mayor

edad=int(input("Ingrese su edad"))

if edad<12:
    print("Es un niño")
elif edad>=12 and edad<=17:
    print ("Es adolescente")
elif edad>=18 and edad<=64:
    print("Es adulto")
else
    print("Es adulto mayor")