from random import randint #Importamos esta librería para randomizar, se  necesita en el loot

#Definicion la función de los combates
def combate(j, e):
    #Presentar al enemigo
    print(" ")
    print("**********NUEVO COMBATE**********")
    print(" ")
    print("Ha aparecido un " + e.nombre)
    print(" ")

    #Inicio combate
    while j.vivo == True and e.vivo == True:
        #Información de estadísticas
        print("*************************")
        print("Tu vida: " + str(j.vida))
        print("Maná que te queda: " + str(j.mana))   
        print("Vida del enemigo: " + str(e.vida))
        print("Poder de ataque de " + e.nombre + ": " + str(e.ataque))


        respuesta = ""
        respuesta = input("¿Qué deseas hacer? a-Atacar (" + str(j.ataque) + ") / c-Curar (coste= " + str(j.costeCuracion) + " , curación= " + str(j.curacion) + "):")
        if respuesta == "a":
            e.quitarVida(j.ataque) #soldado.vida - ataque
            if e.vivo == False:
                break #Para romper el bucle
            
        elif respuesta == "c" and j.mana >= j.costeCuracion: #eslse if
            print("Has decidido curarte")
            j.curar()

        print("El " + e.nombre + " te ataca y te inflige un daño de " + str(e.ataque))
        j.quitarVida(e.ataque)
    if j.vivo == True:
        print("Has vencido a " + e.nombre)
    elif e.vivo == True:
        print(" Te han vencido")
        print("")
        print("***************")
        print("***GAME OVER***")
        print("***************")

#Entrega de loot aleatorio entre las siguientes: cura, recuperar maná y atáque máximo
def loot(personaje):
    if personaje.vivo == True:
        print("Recibes un poco de exp")
        personaje.exp += 100
        print("Recibes 50 monedas de oro")
        personaje.oro += 50
        p = randint(1, 4)
        if p == 1:
            print("Te has curado 25HP")
            personaje.vida += 25
        elif p == 2:
            print("Recargas 25p de maná")
            personaje.mana += 25
        elif p == 3:
            print("Inspeccionas el cadáver y encuentras un amuleto de fuerza: +5 ataque")
            personaje.ataque += 5
        elif p == 4:
            print("Inspeccionas el cadáver y encuentras una bolsita de oro ")
            o = randint (1,3)
            if o == 1:
                print("La bolsa contenía 50 piezas de oro")
                personaje.oro += 50
            elif o == 2:
                print("La bolsa contenía 100 piezas de oro")
                personaje.oro +=100
            elif o == 3:
                print("La bolsa contenía 150 piezas de oro")
                personaje.oro +=150
        