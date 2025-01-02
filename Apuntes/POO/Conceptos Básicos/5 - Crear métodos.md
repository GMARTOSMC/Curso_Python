
Podemos crear los métodos como si fueran funciones. Ejemplo con una clase ya creada, inicializada y definida a la que le añadimos dos métodos:

```python
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
```

