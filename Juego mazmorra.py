import random
import time
suceso=["encontrado una poción", "encontrado una trampa", "encontrado un enemigo"]
vidas=3
ronda_jugador=0
ronda_enemigo=0
pocion=0
combate_ganado=0
combate_perdido=0
trampa=0

print('''      BIENENIDO A LA MAZMORRA DEL TERROR 
      PARA GANAR TIENES QUE GANAR 3 COMBATES
      O MORIR EN EL INTENTO''')
while True:
    ronda_jugador=0
    ronda_enemigo=0
    acción=int(input('''Ingrese la acción que desea hacer
                    1._ Explorar
                    2._ Ver estado
                    3._Salir del juego'''))
    match acción:
        case 1:
            print("Explorar")
            paso=random.choice(suceso)
            print(f"El jugador ha {paso}")
            if paso=="encontrado una poción":
                print(f"+1 de vida. Vida={vidas+1}")
                vidas=vidas+1
                pocion+=1
            elif paso=="encontrado una trampa":
                print(f"-1 de vida. Vida={vidas-1}")
                vidas-=1
                trampa+=1
            elif paso=="encontrado un enemigo":
                print("Pelea!")
                while ronda_jugador!=3 and ronda_enemigo!=3:
                    jugador=input('''Turno del jugador
                                  presiona una tecla''')
                    time.sleep(1)
                    jugador=random.randint(1,6)
                    print(f"Ha salido el numero: {jugador}")
                    print("Turno del enemigo")
                    time.sleep(2)
                    enemigo=random.randint(1,6)
                    print(f"Ha salido el numero: {enemigo}")
                    if jugador>enemigo:
                        print("Ronda del jugador")
                        ronda_jugador+=1
                    elif jugador==enemigo:
                        print("Empate")
                    else:
                        print("Ronda del enemigo")
                        ronda_enemigo+=1
                        
                    if ronda_jugador==3:
                        print("El jugador gana!")
                        combate_ganado+=1
                    elif ronda_enemigo==3:
                        print("El enemigo gana!")
                        print(f"-1 de vida. Vida= {vidas-1}")
                        vidas-=1
                        combate_perdido+=1

            if combate_ganado==3:
                print("FELICIDADES, HAS GANADO!")
                break
            elif vidas==0:
                print("HAS SIDO DERRROTADO")
                break
        case 2:
            print(f"La salud de jugador es: {vidas} ")
            print(f"Pociones encontradas {pocion}")
            print(f"Trampas encontradas: {trampa}")
            print(f"Combates ganados: {combate_ganado}")
            print(f"Combates perdidos: {combate_perdido}")
        case 3:
            break
        case _:
            print("Opción invalida")



