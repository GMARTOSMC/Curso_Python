if para iniciar la condición, elif para más y para la última else. Ejemplo:


```python
edad = 12

if edad < 18 or edad > 30:

    print("No estás en el rando de edad 18-30")  

elif edad <20 or edad > 25:

    print("No estás en el rango de edad 20-25")
  
else:

    print("Estás en el rango de edad entre 18 y 30")
```

Los if se pueden anidar metiendo if dentro de if. Ejemplo:

```python
# Datos del solicitante

edad = 20

promedio = 9.0

ingresos_mensuales = 500

  

# Comprobamos los requisitos para la beca

if edad <= 25:
    if promedio >= 8.5:
        if ingresos_mensuales < 1000:
            print("¡Felicidades! Cumples con los requisitos para la beca.")
        else:
            print("No cumples con los requisitos de ingresos para la beca.")
    else:
        print("No cumples con el promedio necesario para la beca.")
else:
    print("No cumples con el requisito de edad para la beca.")
```


Si tenemos condiciones independientes las unas de las otras, pues simplemente usamos if todo el rato y prescindimos del elif y el else.
