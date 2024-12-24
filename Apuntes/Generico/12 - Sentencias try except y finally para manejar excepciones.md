
Si el usuario no introduce el tipo de dato esperado, se bloqueará el programa. Podemos manejar esto con try y except. Lo que hacemos es englobar las sentencias en las que el usuario lo hace bien dentro del try, y después fuera ponemos except y lo que sucede.

Ejemplo con condicionales:

```
number = input("Please write an integer number\n")  

try:

    number = int(number)
    if (number) % 2 == 0:
        print ("Is even")
    else:
        print ("Is odd")

except ValueError:

    print ("Wrong! You have to write a valid integer number")
```

Con finally lo que esté dentro se ejecuta sí o sí, de error o no.
