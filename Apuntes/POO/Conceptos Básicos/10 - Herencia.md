
***Concepto de Herencia:***

La herencia es un principio de la programación orientada a objetos (POO) que permite crear una nueva clase a partir de una clase existente. La nueva clase, llamada clase derivada o subclase, hereda atributos y métodos de la clase base o superclase, y puede añadir o modificar funcionalidades adicionales. 

***Explicación sencilla:*** 

La herencia permite reutilizar el código de una clase existente, extendiéndola con nuevas características sin tener que modificar la clase original. Es una forma de crear jerarquías y relaciones entre clases.

***Uso del super()***

El super() es una función en Python que se utiliza para llamar métodos de una superclase (clase base) desde una subclase (clase derivada). Es especialmente útil en la herencia para reutilizar y extender la funcionalidad de la clase base y que la subclase herede y extienda sus funcionalidades viendo la reutilización y extensibilidad del código  

Por ejemplo, partiendo de la clase personaje creada en [[4 - Método de inicialización __init__]] y [[5 - Crear métodos]]

Vamos a crear una subclase ***Hechicero***

```python
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
```

Ahora instanciamos la  subclase:


```python
hechicero = Hechicero("Xardas",20, 80, 100, 150)
```

Comprobamos que funciona:


```python
print(hechicero.nombre)  
print(hechicero.atacar("orco"))  
print(hechicero.lanzar_hechizo("bola de fuego", "orco"))
```

Funciona. Y la subclase puede usar tanto los métodos de la clase base como los de la subclase.


