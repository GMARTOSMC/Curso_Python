***Getter***

- ***Definición:*** Un método que permite acceder a un atributo privado desde fuera de la clase. 
- ***Uso:*** Se utiliza para obtener el valor de un atributo privado de manera controlada.

***Setter:***

- ***Definición:*** Un método que permite modificar un atributo privado desde fuera de la clase.
- ***Uso:*** Se utiliza para establecer o cambiar el valor de un atributo privado de manera controlada.

***Ejemplo de método Getter.***

```python
def obtener_nombre(self):  
    return self.__nombre
```

Ahora, si por ejemplo tenemos instanciado un  ***heroe2***  para acceder al nombre simplemente sería:

```python
print(heroe2.obtener_nombre())
```

***Ejemplo de método Setter:***

Por ejemplo para cambiarle el nombre al personaje anterior. Dentro de la clase, porque si nos salimos de la indentación y luego lo ponemos, incluso aunque lo metamos, ya está fuera de la definición. Por tanto importante poner esto ***DENTRO DE LA DEFINICIÓN DE LA CLASE:***

```python
def set_nombre(self, nuevo_nivel):  
    self.__nombre = nuevo_nivel
```

Entonces, ya fuera de la definición de la clase, podemos cambiar el nombre así, por ejemplo si ahora queremos que se llame Merlin:

```python
heroe2.set_nombre("Merlin")
```

Comprobamos que se ha cambiado:

```python
print(heroe2.obtener_nivel())

# Devuelve Merlin
```