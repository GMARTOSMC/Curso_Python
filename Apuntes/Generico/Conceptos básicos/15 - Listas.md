
Una lista es una secuencia de datos ***ordenados*** (La posición importa), ***heterogénea***  (Puede contener distintos tipos de datos) y ***mutable*** (Podemos cambiar la secuencia modificando, eliminando o añadiendo elementos)

Se escriben entre corchetes. Se declaran con ***list***. Por ejemplo:

```python
frutas = ["manzanas", "peras", "naranjas"]

verduras = list["Brocoli", "Zanahorias", "Espinacas"]

```

La lista tiene un orden que va determinado por el orden en el que se introducen los elementos.

Podemos extraer un elemento poniendo en el print corchetes y el número por orden antes de cerrar. Por ejemplo para extraer manzanas en la lista anterior:

```python
print(frutas[0])
```

También negativos. Por ejemplo con -1 sería naranjas con -2 peras, etc.

Puedes cambiar el nombre a un elemento de la lista, por ejemplo para cambiar manzanas por potatos:

```python
frutas[0] = "potatos"
```

***MÉTODOS***

***append*** para agregar elementos al final de una lista:

```python
frutas.append("mandarinas")
```

***count*** para devolver el número de veces que se repite un elemento:

```python
My_List = [2, 5, 5, 288]

print(My_List.count(5))
```

Devuelve 2. Porque el 5 se repite 2 veces.

***index*** Para devolver la posición de la primera aparición de un elemento:

```python
My_List = [2, 5, 5, 288]

print(My_List.index(5))
```

Devuelve 1, porque es la posición de la primera aparición del elemento 5. Recordemos que empieza a contar en 0.

***remove*** para eliminar la primera aparición de un elemento:

```python
My_List = [2, 5, 5, 288]

My_list.remove(5)

print(My_List)

# Devuelve:

[2, 5, 288]
```

Devuelve eso último, ha eliminado el primer 5



