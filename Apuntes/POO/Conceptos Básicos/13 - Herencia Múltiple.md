
La herencia múltiple es una característica en la programación orientada a objetos que permite a una clase heredar atributos y métodos de más de una clase base. Esto puede ser útil para combinar funcionalidades de diferentes clases en una sola clase derivando en una mayor flexibilidad en el diseño de clases.

Ejemplo:


```python
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
```
