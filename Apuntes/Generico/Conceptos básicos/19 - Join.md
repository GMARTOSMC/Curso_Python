
Permite convertir listas en string. Solo funciona si todos los elementos de la lista son string. No funcionará si hay int por ejemplo, o float, etc. Por ejemplo supongamos que tenemos una lista llamada my_list que contiene Y queremos convertirla en una cadena de caracteres que llamaremos, por ejemplo, my_string. Pues la sintaxis sería:

```python
my_string = "".join(my_list)
```

Por ejemplo:

```python
my_list = ["Paco", "Manolo", "Begoña", "Takeshi"]

my_string = "".join(my_list)

print(my_string)
```

Devolverá PacoManoloBegoñaTakeshi

Si lo quisiéramos con espacios entre cada uno, pues simplemente las comillas antes del join tendrían un espacio:

```python
my_list = ["Paco", "Manolo", "Begoña", "Takeshi"]

my_string = " ".join(my_list)

print(my_string)
```

Ahora el print devuelve Paco Manolo Begoña Takeshi
