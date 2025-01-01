
Un diccionario nos permite relacionar pares de elementos clave-valor.

La clave (key) nos permite identificar y buscar el elemento relacionado, que es el valor (value). La key no debe repetirse, si se repite, tomará el valor de la última repetición

Los diccionarios son ***desordenados*** ***heterogéneos*** y con ***clave inmutable*** pero ***el valor es  mutable***. 

El diccionario se forma con llaves. Dentro va la key seguida de dos puntos y el valor relacionado entre comillas. También podemos crearlo con ***dict()***

```python
My_Dic = {1: "Uno", 2: "Dos"}
```

```python
My_Dic = {1: "Uno", 2: "Dos"}
```

Con ***print*** vemos el diccionario:

```python
My_Dic = {1: "Uno", 2: "Dos"}

print(My_Dic)

# Devuelve: 

{1: 'Uno', 2: 'Dos'}
```

Con la key entre corchetes podemos ver el valor asociado a la key:

```python
My_Dic = {1: "Uno", 2: "Dos", 288: "Roto2"}

print(My_Dic[288])

# Devuelve:

Roto2
```

Podemos cambiar o añadir el value de una key con =

```python
My_Dic = {1: "Uno", 2: "Dos"}  

My_Dic[3] = "Tres"

print(My_Dic)

# Devuelve:

{1: 'Uno', 2: 'Dos', 3: 'Tres'}
```


***Métodos:***

- ***keys*** devuelve una lista con las claves. 
- ***values*** devuelve una lista con los valores.
- ***items*** devuelve una lista de tuplas con los pares de datos clave-valor.

```python
print ("---------------------------------------------------------------")
print (my_dict.items())

print ("---------------------------------------------------------------")
print (my_dict.keys())

print ("---------------------------------------------------------------")
print (my_dict.values())
```

Estos tres métodos devuelven vistas dinámicas. Si la guardas en una variable y modificas el diccionario, la variable también es modificada.

***pop*** Para eliminar una clave y su valor:

```python
diccionario.pop(2)
```




