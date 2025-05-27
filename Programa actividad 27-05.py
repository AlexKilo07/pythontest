saldo=100000
total=0
print("Hola, bienvenido")
op=int(input('''Que desea hacer ? 
             1._ Pago de tarjeta de credito
             2._ Simulación de compras
             3._ Salir'''))
while True:
    match op:
        case 1:
            print("Pago de tarjeta de credito")
            print("Tiene una deudad de $100.000")
            op2=int(input("Desea pagar su deuda? 1._Si, 2._No"))
            match op2:
                case 1:
                    deuda=int(input("Ingrese el monto que desea pagar"))
                    while deuda>=0 and deuda<=100000:
                        print(f"Su deuda actual es de $ {saldo-deuda}")
                case 2:
                    print("Volviendo al menú principal")
        case 2:
            print("Simulacion de compras")
            while True:
                compra=("Ingrese el monto de la compra que desea hacer o pulse la letra f para salir")
                while compra>=0 and compra!="f":
                    print(f"El total de su compra es $ {total+compra}")
            
                print("Volviendo al menú principal")

                    

