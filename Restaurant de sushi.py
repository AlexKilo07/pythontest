desc=0
clave="soyotaku"
producto=0
pikachu=0
anguila=0
pulpo=0
otaku=0
total=0
print("Hola, bienvenido a Sushi Restaurant")
opc=int(input('''Que desea pedir ?
              1._Pikachu Roll $4500
              2._Otaku Roll $5000
              3._Pulpo Venenoso Roll $5200
              4._Anguila Electrica Roll $4800
              5._Siguiente..'''))
while opc !=5:
    opc=int(input('''Que desea pedir ?
              1._Pikachu Roll $4500
              2._Otaku Roll $5000
              3._Pulpo Venenoso Roll $5200
              4._Anguila Electrica Roll $4800
              5._Siguiente..'''))
    match opc:
        case 1:
            print("Usted ha seleccionado Pikachu Roll")
            total+=45000
            pikachu+=1
            producto+=1
        case 2:
            print("Usted ha seleccionado Otaku Roll")
            total+=5000
            otaku+=1
            producto+=1
        case 3: 
            print("Usted ha seleccionado Pulpo Venoso Roll")
            total+=5200
            pulpo+=1
            producto+=1
        case 4:
            print("Usted ha seleccionado Anguila Electrica Roll")
            total+=4800
            anguila+=1
            producto+=1
        case 5:
            break 
        case _:
            print("Error, seleccione una opción valida")
op2=int(input('''Posee codigo de descuento?
          1._Si
          2._No'''))
if op2==1:
    desc=input("Ingrese su codigo de descuento")
    if desc==clave:
        while True:
            desc=input("Ingrese su codigo de descuento")
            if desc==clave:
                print("Descuento realizado")
                desc=total*0.1
                total=total-desc
                break
    else:
        print("Codigo invalido")
        nu=input("Desea intentar nuevamente? 1._Si 2._No"))
        if nu==1:
        
else:
    print("Generando boleta")
print(f'''El total de productos es {producto}: 
          Pikachu Roll {pikachu}, 
          Otaku Roll {otaku}, 
          Pulpo venoso Roll {pulpo}, 
          Anguila Electrica Roll {anguila}
          --------------------------------
          Total por pagar: {total}
          Descuento aplicado {desc}''')






