total=0
carrito=0
while True:
    op=int(input('''Seleccione una opcion
        1.-Ingresar Nombre
        2.-Comprar
        3.-Mostrar boleta
        4.-Salir
        '''))
    match op:
        case 1:
            nombre=input("Ingrese su nombre")
        case 2:
            while True:
                producto=int(input('''Ingrese el producto que desea:
                                   1._ Playstation $15000
                                   2._ Xbox $12000
                                   3._ Nintendo $10000
                                   4._ PC $ 20000
                                   5._ Salir'''))
                match producto:
                    case 1:
                        print("Usted ha seleccionado una Playstation")
                        total+= 15000
                    case 2:
                        print("Usted ha seleccionado una Xbox")
                        total+= 12000
                    case 3:
                        print("Usted ha seleccionado una Nintendo")
                        total+= 10000
                    case 4:
                        print("Usted ha seleccionado una PC")
                    case 5:
                        break
                    case _:
                        ("Producto no valido" )
                print("Su total parcial es de: ", total)
                carrito+=1
        case 3:
            print(f'''El total de articulos de su compra es: {carrito} 
                      El total neto de su compra es: {total} 
                      El total de su compra mas IVA es: {total*1.19}
                      Gracias {nombre} por venir a nuestra tienda
                      Vuelva pronto.''')
        case 4:
            break
        case _:
            ("Opcion no valida")
                    
                

    