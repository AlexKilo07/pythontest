cant=int(input("Ingrese el numero de votantes"))

kaiser=0
kast=0

for i in range(cant):
        print("Ingrese su voto: Kaiser 1, 2 Kast")
        voto=int(input())
        if voto==1:
                kaiser=kaiser+1
        elif voto==2:
                kast=kast+1
        else:
            print("Error, selecccione un voto valido")
print("Los votos de Kaiser son: ", kaiser)
print("Los votos de Kast son: ", kast)
if kaiser>kast:
    print("Ganó Kaiser")
else:
      print("Ganó Kast")
    
