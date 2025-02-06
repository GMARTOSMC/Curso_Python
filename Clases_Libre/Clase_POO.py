# Creacion de una clase
class Personaje:
    # Metodo de inicialización
    def __init__(self, nombre, clase, nivel, salud, mana):
        # Atributos de la clase
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.salud = salud
        self.mana = mana

    # Metodo para atacar a un objetivo

    def atacar(self, objetivo):
        return f"{self.nombre} ataca a {objetivo}!"

    # Metodo para curarse a si mismo

    def curar(self, cantidad):
        self.salud += cantidad
        return f"{self.nombre} se cura {cantidad} puntos de salud."

# Instanciación de un objeto de la calse Personaje
heroe = Personaje("Ivespino", "Guerrero", 10, 100, 50 )
# Uso de los métodos del objeto
print(type(heroe))
print(heroe.atacar("Orco"))
print(heroe.curar(20))

# Como los atributos no están encapsulados es fácil acceder a ellos

print(heroe.clase)
# Creamos clase con atributos privados

class Personaje2:
    # Metodo de inicialización
    def __init__(self, nombre, clase, nivel, salud, mana):
        # Atributos de la clase
        self.__nombre = nombre
        self.__clase = clase
        self.__nivel = nivel
        self.__salud = salud
        self.__mana = mana

    # Para los métodos simplemente incluímos las barras bajas en el llamado al atributo

    # Metodo para atacar a un objetivo

    def atacar(self, objetivo):
        return f"{self.__nombre} ataca a {objetivo}!"

    # Metodo para curarse a si mismo

    def curar(self, cantidad):
        self.__salud += cantidad
        return f"{self.__nombre} se cura {cantidad} puntos de salud."

### METODOS GETTER Y SETTER

    # Para obtener el nombre usando metodo getter

    def obtener_nombre(self):
        return self.__nombre

    # Metodo para obtener la salud del personaje

    def obtener_salud(self):
        return self.__salud

    # Metodo para obtener el nivel del personaje

    def obtener_nivel(self):
        return self.__nivel

    # Metodo para cambiar el nivel del personaje

    def set_nivel(self, nuevo_nivel):
        self.__nivel = nuevo_nivel


### INSTANCIACIÓN DE UN OBJETO DE LA CLASE PERSONAJE

heroe2 = Personaje2("Gandalf", "Mago", 10, 100, 50 )

# Como ya hemos creado los metodos getter, ya podemos hacerlo simplemente llamando al metodo

# Llamamos a los metodos anteriores

# Nombre

print(heroe2.obtener_nombre())

# Nivel

print(heroe2.obtener_nivel())

# Establecer nivel en 12

heroe2.set_nivel(12)

# Comprobar que ha cambiado el nivel

print(heroe2.obtener_nivel())

# Salud

print(heroe2.obtener_salud())

### HERENCIA

# Creamos subclase de la clase base Personaje

class Hechicero(Personaje):
    def __init__(self, nombre, nivel, salud, mana, poder_magico):
        super().__init__(nombre, "Hechicero", nivel, salud, mana)
        self.poder_magico = poder_magico

    def lanzar_hechizo(self, hechizo, objetivo):
        if self.mana > 0:
            self. mana -= 10
            return f"{self.nombre} lanza {hechizo} a {objetivo} con poder {self.poder_magico}!"
        else:
            return f"{self.nombre} no tiene suficiente mana para lanzar {hechizo}."

# Instanciamos la subclase

hechicero = Hechicero("Xardas",20, 80, 100, 150)

# Comprobamos que funciona

print(hechicero.nombre)
print(hechicero.atacar("orco"))
print(hechicero.lanzar_hechizo("bola de fuego", "orco"))

### SOBREESCRITURA DE METODOS

# Clase derivada guerrero

class Guerrero(Personaje):
    def __init__(self, nombre, nivel, salud, mana, fuerza):
        super().__init__(nombre, "Guerrero", nivel, salud, mana)
        self.fuerza = fuerza

        # Sobreescritura del metodo atacar

    def atacar(self, objetivo):
        return f"{self.nombre} ataca ferozmente a {objetivo} con fuerza {self.fuerza}!"

guerrero = Guerrero("Bruenor",20, 80, 100, 150)

print(hechicero.atacar("orco"))
print(guerrero.atacar("orco"))

### POLIMORFISMO

# Uso del polimorfismo:

def realizar_ataque(personaje, objetivo):
    print("¡Te lanzaré mi mejor golpe!")
    print(personaje.atacar(objetivo))

realizar_ataque(hechicero, "orco")
realizar_ataque(guerrero, "orco")

### HERENCIA MÚLTIPLE

# Clase base 1

class Barbaro:
    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud

    def atacar(self, objetivo):
        return f"{self.nombre} ataca a {objetivo}!"

    # Clase base 2

class Conjurador:
    def __init__(self, nombre, mana, poder_magico):
        self.nombre = nombre
        self.mana = mana
        self.poder_magico = poder_magico

    def lanzar_hechizo(self, hechizo, objetivo):
        if self.mana > 0:
            self. mana -= 10
            return f"{self.nombre} lanza {hechizo} a {objetivo} con poder {self.poder_magico}!"
        else:
            return f"{self.nombre} no tiene suficiente mana para lanzar hechizos"

# Clase derivada con herencia múltiple

class GuerreroMago(Barbaro, Conjurador):
    def __init__(self, nombre, nivel, salud, mana, poder_magico, fuerza):
        Barbaro.__init__(self, nombre, nivel, salud)
        Conjurador.__init__(self, nombre, mana, poder_magico)
        self.fuerza = fuerza

    def atacar_con_fuerza(self, objetivo):
        return f"{self.nombre} ataca a {objetivo} con fuerza {self.fuerza}!"

guerrero_mago = GuerreroMago("Ratloz", 10, 100, 50, 80, 200 )

print(guerrero_mago.atacar("orco"))
print(guerrero_mago.lanzar_hechizo("Fuego", "orco"))
print(guerrero_mago.atacar_con_fuerza("orco"))
