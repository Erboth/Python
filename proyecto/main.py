from personajes import Enemigo, Personaje, Soldado, Arquero, Sargento
from control import combate, loot
from random import randint

#Propiedades del PJ
jugador = Personaje("", 100, 15, 100, 25, 30)

#Bienvenida al juego
print("El texto de introdución...")
jugador.nombre = input("Introduce tu nombre de jugador ")
print ("Bienvenido al mundo de Dungeons and Dragons " +  jugador.nombre)

#Primer nivel
nivel1 = [Soldado(randint(0, 2)), Arquero(randint(0, 2)), Soldado(randint(0, 2)), Sargento(randint(0, 2))] #Array de los enemigos que salen en el nivel que se busacan en personaje.py

for enemigo in nivel1:
    combate(jugador, enemigo)
    loot(jugador)
    jugador.comprobarNivel()
    
if jugador.vivo == True:
    print("¡¡¡¡¡HAS SUPERADO LA SALA!!!!!")