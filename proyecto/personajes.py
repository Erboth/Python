class Enemigo:
    #Definimos una función que pertenece a la clase Enemigo y le damos las características que va a buscar al crear los enemigos
    def __init__(self, nombre, vida, ataque, lvl): 
        self.nombre = nombre
        self.vida = vida +5*lvl
        self.ataque = ataque +2*lvl
        self.vivo = True #True para decir que sí está vivo
        self.lvl = lvl

    #Método para perder vida
    def quitarVida(self, cantidad):
        if self.vivo == True:
            self.vida -= cantidad
            if self.vida <= 0:
                self.vivo = False #Si la vida es menor a cero está muerto, por lo cual vivo = False

class Soldado (Enemigo): #Hereda de la clase superior enemigo
    def __init__(self, lvl):
        super().__init__("Soldado", 35, 6, lvl) #Super se refiere a la clase superior( en este caso enemigo)

class Arquero (Enemigo): 
    def __init__(self, lvl):
        super().__init__("Arquero", 28, 8, lvl)

class Sargento (Enemigo): 
    def __init__(self, lvl):
        super().__init__("Sargento", 40, 10, lvl)

class Personaje:
    def __init__(self, nombre, vida, ataque, mana, curacion, costeCuracion):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.mana = mana
        self.curacion = curacion
        self.costeCuracion = costeCuracion
        self.vivo = True #No está dentro de def porque no preguntas al crear un personaje si está vivo o muerto
        self.exp = 0
        self.lvl = 1
        self.oro = 50
        self.expSiguenteNivel = 150

    def quitarVida(self, cantidad):
        if self.vivo == True:
            self.vida -= cantidad
            if self.vida <=0:
                self.vivo = False
    
    def curar(self):
        self.vida += self.curacion
        self.mana -= self.costeCuracion

    def comprobarNivel (self):
        if self.exp >= self.expSiguenteNivel:
            self.lvl += 1
            self.expSiguenteNivel = 550
            self.vida += 10 #Cada nivel subido la característica se multiplica por 1.1
            self.ataque += 5
            self.mana +=10
            print("¡¡¡Has subido de nivel!!! Tu nuevo nivel es: " + str(self.lvl))
            print("Ahora tu vida es de: " + str(self.vida))
            print("Ahora tu ataque es de: " + str(self.ataque))
            print("Ahora tu maná es de: " + str(self.mana))