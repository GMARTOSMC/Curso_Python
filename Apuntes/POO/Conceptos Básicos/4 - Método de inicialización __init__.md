El método de inicialización  ***(__init__)***  es una función especial en una clase que se ejecuta cuando se crea un nuevo objeto. Se utiliza para establecer los valores iniciales de los atributos del objeto. 

Ejemplo de creación e inicialización de una clase para un personaje de un rpg:

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
```



