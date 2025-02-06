
Un conjunto es una colección de elementos únicos y desordenados. Se forman con llaves, o con paréntesis y set

Es recomendable usar siempre set porque los diccionarios también se crean con llaves.

Si usamos set, es necesario declarar que tipo de set queremos, añadiendo el componente necesario, por ejemplo como una lista con corchetes, una tupla con paréntesis, etc

```python
Set_Vacio = set()

My_Set_Tuple = set((2, "Paco", 288))

My_Set_List = set([4, 67, "Hola"])

My_Set = {4, 288, "Hola"}
```

Uno de sus usos es eliminar elementos repetidos de una secuencia. Ejemplo:


```python
My_Set = set((2, 3, 3, 288))

print(My_Set)

# Devuelve:

{2, 3, 288}
```

***Métodos***

***add*** para añadir elemento al principio:


```python
My_Set = set((2,3,4))

My_Set.add(1)
```

***remove*** Para eliminar elementos:

```python
My_Set = set((2,3,4))

My_Set.remove(3)
```

