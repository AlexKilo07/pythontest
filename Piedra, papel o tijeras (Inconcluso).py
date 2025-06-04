import random

print("Piedra, papel o tijeras")
opciones=["papel", "piedra", "tijeras"]

maquina=random.choice(opciones)
jugador=0


while jugador!=4:
    try:
       jugador=int(input('''Ingrese una opcion: 
            1._Piedra, 2._Papel, 3._Tijeras 4._Salir'''))
    except Exception as e:
          print(f"solo puede digitar enteros {e}")

    # print(f"La maquina ha seleccionado {maquina}")
    # if jugador==1:
    #      jugadoraux="piedra"
    # elif jugador==2:
    #      jugadoraux="papel"
    # elif jugador==3:
    #      jugadoraux="tijeras"
    # elif jugador==4:
    #      break
    # else:
    #      print("Opcion invalida")

    # if jugadoraux==maquina:
    #      print("Empate!")
         
    
