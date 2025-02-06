#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'ñ', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'Ñ', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
print("Made by Gonzalo Martos Conesa")

# Lo hago dentro de un while porque quiero poder reiniciar si el usuario ingresa mal los datos

while (True):
    try:
        
        nr_letters= int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        
        # Inicializamos la variable password para asegurarnos de que sea un string
        # Necesitamos que sea string para que concatene como queremos
        # Y además porque si no mi método de randomizarlo no va a funcionar
        
        password = ""
        
        # El último en el rango no se incluye, por eso + 1 para incluirlo y que el bucle for se ejectue el mismo
        # número de veces que el valor de la variable nr_letters
        # Usamos un contador para guardar en la variable string que creamos el resultado
        # La idea es concatenarlo con el resto de la contraseña random
        
        for letter in range(1, nr_letters + 1):
            random_letter = random.choice(letters)
            password += random_letter
        
        #repetimos para guardar los números y símbolos
        
        for number in range(1, nr_numbers + 1):
            random_number = random.choice(numbers)
            password += random_number
            
        for symbol in range(1, nr_symbols + 1):
            random_symbol = random.choice(symbols)
            password += random_symbol
        
        # Ahora tenemos que randomizar el string resultante, random.shuffle hace eso
        # El problema es que solo funciona con listas. Tenemos que convertir el resultado en lista
        # Y luego volver a convertirlo en string.
        
        #Lista es list, por tanto podemos simplemente convertirlo como cualquier otro tipo de dato:
        
        password = list(password)
        
        # Ahora podemos usar random.shuffle para randomizarlo:
        
        random.shuffle(password)
        
        # Ahora hay que devolverlo a string. Para ello hay que usar join:
        
        password = "".join(password)
        
        # Ahora con un f string debería poder concatenarse y devolver la contraseña entera junta
        
        print(f"Your password is: {password}")
        break
    
    # Quiero avisar al usuario y reiniciar el bucle si ingresa mal los datos
    
    except ValueError:
        print("Please, type a valid number")
        continue
