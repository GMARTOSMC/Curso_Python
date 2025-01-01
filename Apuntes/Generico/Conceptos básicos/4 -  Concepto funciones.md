
Las funciones son bloques de código que te permiten reutilizarlo. 

Las funciones van seguidas de paréntesis y dentro de los paréntesis van los parámetros de ser necesarios.

Podemos crear funciones con las palabra reservada def:


```python
def mi_funcion():
	print("Hola)
	print("Adios)
```

Lo que va en la indentación será la función. Para salir simplemente salimos de la indentación.

Los parámetros van con las definiciones, los argumentos con las llamadas.

Para llamar la función anterior sería el nombre de la función y paréntesis, con los argumentos de ser necesarios:


```python
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













