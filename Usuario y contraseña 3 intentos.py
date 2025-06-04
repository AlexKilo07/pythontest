intentousuario=0
intentoclave=0
usuario="alexanderuc13"
clave="alexkilo07"
user= ""
contraseña=""

while usuario!=user:
    user=input("Ingrese su usuario")
    if intentousuario>2:
        print("Demasiados intentos, usuario bloqueado")
        break
    intentousuario+=1
while contraseña!=clave and user==usuario:
        contraseña=input("Ingrese su contraseña")
        if intentoclave>2:
            print("Demasiados intentos, usuario bloqueado")
        elif contraseña==clave:
            print("Bienvenido")
        intentoclave+=1
#    else:
#        contraseña=input("Ingrese su contraseña")

