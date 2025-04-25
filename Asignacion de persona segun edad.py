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
else:
    print("Es adulto mayor")