
Podemos crear una lista que contenga varias listas. Ejemplo:

```python
frutas = ["manzanas", "peras", "naranjas"]
verduras = ["tomates", "zanahorias", "brocoli"]

frutas_y_verduras = [frutas, verduras]
```

Para seleccionar elementos de la lista, primero seleccionamos de que lista y luego el elemento. Por ejemplo, para seleccionar zanahorias, es 1, para seleccionar verduras, y 1 para zanahorias dentro de verduras. Pasando a código:

```python
print(frutas_y_verduras[1][1])
```


También si están sin declarar:

```python
nested_list = ["A", "B", ["C", "D"]]  
print(nested_list[2][1])
```
