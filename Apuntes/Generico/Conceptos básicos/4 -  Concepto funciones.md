mi_funcion()
```

Devolvemos valores calculados con la sentencia ***return*** 

Por ejemplo. Supongamos que queremos calcular la media de los tres últimos exámenes:

```python
def media(num_1, num_2, num_3):
	resultado = num_1 + num_2 + num_3
	resultado = resultado / 3
	return resultado

llamada = media(5,7,9)

print(llamada)

# Devuelve:

7.0
```

***return*** va acompañado de un valor, ya sea una variable o una expresión. Es más claro con variables pero en sí se podría hacer  lo mismo prescindiendo de las variables:

```python
def media(num_1, num_2, num_3):
	return (num_1 + num_2 + num_3) / 3

llamada = media(5,7,9)

# Devuelve:

7.0
```


Explicación sencilla de parámetro y argumento:

![[parametros_argumentos.png]]



Podemos especificar la clave en el argumento al llamar a la función para que, aunque cambiemos el orden, se llamen correctamente. Ejemplo:

```python
def nombre_direccion(name,location):  
    print(f"Hello, {name}")  
    print(f"What is it like in {location}")  
  
nombre_direccion(location = "Cartagena", name = "Gonzalo")

# Devuelve

Hello, Gonzalo
What is it like in Cartagena
```

En el ejemplo hemos invertido los argumentos, pero como especificamos la clave en el argumento al llamarla, funciona igual.



