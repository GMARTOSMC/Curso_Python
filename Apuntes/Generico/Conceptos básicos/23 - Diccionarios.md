
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
- ***get*** devuelve el valor de una clave específica

```python
print ("---------------------------------------------------------------")
print (my_dict.items())

print ("---------------------------------------------------------------")
print (my_dict.keys())

print ("---------------------------------------------------------------")
print (my_dict.values())
```

Estos tres métodos devuelven vistas dinámicas. Si la guardas en una variable y modificas el diccionario, la variable también es modificada.

El método get por ejemplo para encontrar el ganador de la subasta:

```python
`users = {'Alice': 100, 'Bob': 200, 'Charlie': 150}`
winner_name = max(users, key=users.get)


***pop*** Para eliminar una clave y su valor:

```python
diccionario.pop(2)
```

Para vaciar un diccionario simplemente le asignamos un diccionario vacío:

```python
My_Dic = {}
```

También podemos crear un diccionario vacío de la misma forma.

Si un bucle for recorre el diccionario, por defecto recogerá los valores de las claves, no de los elementos.

Por ejemplo:

```python
for thing in My_Dict:
	print(thing)
```

Devuelve las claves. Si queremos que devuelva los elementos tenemos que poner:

```python
for thing in My_Dict:
	print(My_Dict[thing])
```

Cuando usamos for con un diccionario, y queremos iterar en el elemento, debemos usar el método items, y darle dos parámetros, el primero es la clave el segundo el valor.
De lo contrario solo iterará la clave.
Ejemplo:

```python
student_scores = {  
    'Harry': 88,  
    'Ron': 78,  
    'Hermione': 95,  
    'Draco': 75,  
    'Neville': 60  
}  
  
student_grades = {}  
  
for score, value in student_scores.items():  
    if value > 90:  
        student_grades[score] ="Outstanding"  
  
print(student_grades)
```

Podemos anidar listas y tuplas dentro de un diccionario. Por ejemplo, tenemos el diccionario ***travel_log*** con claves de países y elementos que son listas de ciudades de esos países. Para acceder a una ciudad, buscados en el diccionario con la clave del país y luego el número del elemento de la lista. Por ejemplo: 

```python
travel_log = {  
    "France":["Paris", "Lille", "Dijon"],  
    "Germany":["Stuttgart", "Berlin"],  
}  
  
# Imprimir "Lille"  
  
print(travel_log["France"][1])
```

También podemos anidar diccionarios dentro de un diccionario. EJemplo:

```python
travel_log = {  
    "France": {  
        "cities visited": ["Paris", "Lille", "Dijon"],  
        "num_times_visited": 12,  
    },  
    "Germany": {  
        "cities visited": ["Stuttgart", "Berlin"],  
        "num_times_visited": 5,  
    }  
}  

# Print Berlin:

print(travel_log["Germany"]["cities visited"][1])
```

[[6 - Bucle For]]
