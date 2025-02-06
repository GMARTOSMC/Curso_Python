import art
print(art.logo)

#inicializamos el diccionario
users = {}
more_bidders = True

# El bucle principal
while more_bidders == True:
    # El nombre es la clave, el precio el valor
    name = input("What's your name?\n")
    prize = int(input("How much do you bid?\n"))
    users[name] = prize

    # Preguntamos si hay más usuarios
    more_users = input("There are more bidders? Type yes or no\n").lower()
    if more_users == "yes":
        more_bidders = True
    else:
        more_bidders = False

    # Ocultamos la respuesta anterior
    print("\n" * 40)

# Determinamos el ganador
winner_name = max(users, key=users.get)
highest_bid = users[winner_name]

# Mostramos el resultado
print(f"The winner is {winner_name} with a bid of ${highest_bid}.")
print("Thank you for playing!")
input("Press enter to quit")
