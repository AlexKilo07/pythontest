# Preguntar al usuario cuantos productos llevará
# escribir listado de 3 productos y sus precios
# mostrar el total neto de la compra
# y mostrar el total mas IVA (19%)

cant=int(input("Cuantos productos llevará?"))
total=0

for i in range (cant):
       print('''
       Que producto llevará?
	   1.- Diazepam $9000
	   2.- Metametozona $18500
	   3.- Oblea China $1000" ''')
       op=int(input())
       if op==1:
           print("Usted llevará Diazepam")
           total=total+9000
       elif op==2:
             print("Usted lleva Metamezatona")
             total=total+18500
       elif op==3:
           print("Usted lleva Oblea China")
           total=total+1000
       else:
            print("Opción no valida")
print("El total neto es ", total)
print("El total mas IVA es ", total*1.19)
     