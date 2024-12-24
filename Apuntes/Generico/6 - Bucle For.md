creo la variable my_list con una lista, luego  creo la variable number para el for. Al imprimir la variable number creada con el bucle for nos muestra los números de la lista.

```python
my_list = [2,4,5,6,7,8]

  

for number in my_list:

    print(number)
```



¿Qué hace? la variable creada number lo que hace es recorrer toda la lista en bucle, desde el primer elemento hasta el último. Entonces, primero saca el 2, luego el 4, etc. 

Si por ejemplo, queremos que saque el número más grande, pues haríamos:

```python
my_list = [2,4,5,6,7,8]

larguest = 0

for number in my_list:
	if number > larguest:
		larguest = x
print(larguest)

```

¿Por qué? Fijémonos. Hemos creado una lista, luego inicializamos la variablle larguest como un int de valor 0. Luego decimos que en bucle for, la variable number recorre la lista. Si un elemento de esa lista, que ahora está en la variable number porque es la que lo recorre, es más grande que larguest, ahora larguest es ese número.

De esa forma se comparan todos con larguest, y cuando es más grande se asigna, si no no pasa nada, por tanto al final queda larguest = al mas grande.

También podemos usar el bucle for con un rango. Por ejemplo:

```python
for number in range (1,5):
	print(number)
```

La variable ***number*** recorre todo el rango de 1 a 4 y devolverá 1, 2, 3 y 4. Hay que tener en cuenta que ***range*** NO incluye el límite superior. Por eso es de 1 a 4.







