Choice elige un elemento al azar de la lista
Supongamos lista frutas. Sintaxis:

```python
random.choice(frutas)
```

Retornará un elemento al azar de la lista.

Choices nos permite elegir varios, y además dar parámetros que cambien la probabilidad. 

***weights*** Se usa para la probabilidad de que salga cada uno. ***k*** nos permite establecer el número de elementos que queremos que salgan. Téngase en cuenta que con este método se puede repetir elemento.

Por ejemplo:

```python

mylist = ["apple", "banana", "cherry"]  
  
print(random.choices(mylist, weights = [10, 1, 1], k = 14))
```



Esto devuelve 14 elementos de esa lista aleatoriamente, y hay 10 veces más probabilidades de que salga ***apple*** que el resto.





