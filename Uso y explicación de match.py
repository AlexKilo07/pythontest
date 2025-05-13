# Uso y explicaión de match

def suma():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la suma es ", n1+n2)

# suma()

def resta():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la resta es ", n1-n2)

# resta()

def multiplicación():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la multiplicación es ", n1*n2)

# multiplicación()

def división():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la resta es ", n1/n2)

# división()

def calcu():
    while True:
        op=int(input("""Ingrese una operación: 
             1._ Suma, 
             2._ Resta, 
             3._ Multiplicación
             4._ División
             5._ Salir"""))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multiplicación")
                multiplicación()
            case 4:
                print("División")
                división()
            case 5:
                print("Saliendo")
                break
            case _:
                print("Error, ingrese un numero valido")


calcu()