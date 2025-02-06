
El polimorfismo es un concepto fundamental en la programación orientada a objetos (POO) que permite que objetos de diferentes clases sean tratados como objetos de una clase común. Esto se logra a través de la herencia y la sobreescritura de métodos. El polimorfismo permite que el mismo método se comporte de manera diferente en diferentes clases.

***Explicación sencilla:***

El polimorfismo permite usar una interfaz común para diferentes tipos de objetos. Por ejemplo, diferentes clases pueden implementar un método ***atacar*** de manera distinta, pero se puede llamar a ***atacar*** en cualquiera de estos objetos de la misma manera aunque sean de distintas clases.

Ejemplo:

```python
def realizar_ataque(personaje, objetivo):  
    print("¡Te lanzaré mi mejor golpe!")  
    print(personaje.atacar(objetivo))  
  
realizar_ataque(hechicero, "orco")  
realizar_ataque(guerrero, "orco")
```

Obviamente el ataque será diferente según hayamos configurado cada clase.


