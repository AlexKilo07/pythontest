#Asignación por edad#

edad=int(input("Ingrese su edad"))

if edad<12:
    print("Usted es un niño")
elif edad>=12 and edad<18:
    print("Usted es adolescente")
else:
    print("Usted es mayor de edad")