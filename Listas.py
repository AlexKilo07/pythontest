cont=0
nombres=["Cristopher", "Steven"]
apellidos=["Nolan", "Spilverg"]
while True:
    op=int(input('''Seleccione una opcion:
                 1._Ingresar nombre
                 2._Buscar nombre
                 3._Mostrar lista
                 4._Salir'''))
    match op:
        case 1:
            nom=input("Ingrese un nombre")
            nombres.append(nom)
            print(nombres) 
            ape=input("Ingrese un apellido")
            apellidos.append(ape)
            print(apellidos) 
        case 2:
            busca=input("Ingrese el nombre a buscar")
            if busca in nombres:
                print(f"El nombre {busca} existe en la lista")
            else:
                print(f"El nombre {busca} no existe en la lista")
        case 3:
            cont=0
            # for n in nombres:
            #     print(cont+1,",-", nombres[cont, apellidos[cont]])
            #     cont+=1
            for i in range(len(nombres)):
                print(i+1,"._",nombres[i], apellidos[i])
        case 4:
            break
            