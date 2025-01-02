
La sobreescritura de métodos es una técnica en la programación orientada a objetos (POO) donde una subclase proporciona una implementación específica de un método que ya está definido en su superclase. Esto permite que la subclase modifique o extienda el comportamiento del método de la clase base a el comportamiento de los métodos heredados de la superclase.

Básicamente nos permite que el mismo método haga cosas distintas según la clase.

Ejemplo en el que sobreescribimos el método atacar:

```python
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
 
print(guerrero.atacar("orco"))
```

