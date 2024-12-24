# Imprimir por pantalla un menú para poder
# Seleccionar una de las siguientes operaciones:
# Suma, resta, multiplicación y división
# El programa te dirá por pantalla y mostrará el resultado final de la operación

# 1 es para suma, 2 es para resta, 3 es para multiplicación, 4 es para división

print("Bienvenido a esta calculadora simple")

def calculadora (num1,num2,operacion):


    if operacion == 1:
        print(f"El resultado de {num1} + {num2} es igual a {num1 + num2}" )
    
    elif operacion == 2:
        print(f"El resultado de {num1} - {num2} es igual a {num1 - num2}")
    elif operacion == 3:
        print(f"El resultado de {num1} x {num2} es igual a {num1 * num2}")
    
    elif operacion == 4:
        print(f"El resultado de {num1} / {num2} es igual a {num1 / num2}")
    
    else: print("Mal elegido")

eleccion = int(input("Elige 1 para suma, 2 para resta, 3 para multiplicación, 4 para división\n"))

numero1 = float(input("Elige un número para operar\n"))

numero2 = float(input("Elige otro número para operar\n"))

calculadora(numero1,numero2,eleccion)