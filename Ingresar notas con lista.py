# Tarea
# Crear programa de manejo de notas
# 1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostar notas
# 4.- Sacar promedio, nota mayor y nota menor
# 5.- Limpiar todas las notas
# 6.- Salir

notas=[7.0,4.6,4.9, 7.0,5.6]

while True:
    while True:
        try:
            print('''   

                1.- ingresar notas
                2.- borrar nota
                3.- ver notas colocadas
                4.- promedio de notas, nota mayor y nota menor
                5.- borrar toda las notas
                6.- salir
                    ''')
            op=int(input())
            break
        except Exception:
            print("Debe ingreser un numero entero valido")
    

    match op:
        case 1:
            nota=float(input("ingrese la nota del alumno: "))
            notas.append(nota)
        case 2:
            for num, n in enumerate(notas):
                print(num+1,".- ",n)
            elim=int(input("ingrese cual quiere eliminar: "))
            notas.pop(elim-1)
        case 3:
            print(notas)
        case 4:
            if len(notas) == 0:
                print("No hay notas para calcular el promedio.")
            else:
                promedio=sum(notas)/len(notas)
                print(f"El promedio de las notas es: {round(promedio, 1)}")
                print("la nota mayor es", max(notas))
                print("la nota menor es", min(notas))
        case 5:
            notas.clear()
        case 6:
            print("saliendo...")
            break
        case _:
            print("ya wey escoge algo valido")