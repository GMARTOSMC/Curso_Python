print("Bienvenido al calculador de factura. Aquí calcularemos cuanto tiene que pagar cada uno")

factura_inicial = float(input("¿De cuanto es la factura? Usa punto en lugar de  coma para los decimales."))

propina = float(input("¿Qué porcentaje de la factura quieres dejar como propina? Escribe solo el número, sin el porcentaje."))

# El resultado será float si alguna de las varaibles lo es

factura_total = (factura_inicial + (factura_inicial * propina / 100))

personas = int(input("¿Cuántos sois?"))

resultado = (factura_total / personas)

# Redondeamo a 2 decimales

resultado_redondeo = round(resultado, 2)

# De esta forma usamos f-string, todo va dentro de las mismas comillas dobles y las variables que no son string entre corchetes

mensaje = f"Cada uno debe pagar {resultado_redondeo}€"

print(mensaje)

