
Se engloba el bucle dentro de ***while***. Se usa ***break*** para cerrar y ***continue*** para reiniciar.

Ejemplo con [[9 - Condicional if]] y [[12 - Sentencias try except y finally para manejar excepciones]]

```python
while(True):

    try:

        number = input("Please write an integer number\n")

        number = int(number)

        if (number) % 2 == 0:

            print ("Is even")

            break

        else:

            print ("Is odd")

            break

    except ValueError:

        print ("Wrong! You have to write a valid integer number")

        continue

print("End of the program")
```