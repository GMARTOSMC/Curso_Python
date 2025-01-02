import random, hangman_art as h_art, hangman_words as h_words
print(h_art.logo)

chosen_word = random.choice(h_words.word_list)
word_length = len(chosen_word)

print("Welcome to hangman game")
print("Made by Gonzalo Martos Conesa")
# Inicializar el display
display = ["_"] * word_length
current_progress = "".join(display)
print("".join(display))
lives = 6

# Bucle principal
while "_" in display:

    print(f"Yoy have {lives} lives left.")
    # Pedimos la letra y la guardamos en la variable
    guess = input("Guess a letter: ").lower()

    # Al fallar

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word")
        print("You lose a life")

    # Comprobamos que no repite letra ya acertada:

    if guess in display:
        print(f"{guess} is already in the word")

    # Mostramos la etapa del dibujo según las vidas

    print(h_art.stages[lives])

    # Derrota

    if lives == 0:
        print(f"The word was {chosen_word}")
        print("Sorry you Lose")
        print("Game Over")
        break
    # Actualizamos el display al acertar

    for letter in range(word_length):
        if chosen_word[letter] == guess:
            display[letter] = guess  # Reemplazar guión por la letra acertada

    # Mostrar el progreso actualizado
    current_progress = "".join(display)
    print(current_progress)

    # Para ganar

if current_progress == chosen_word:
    print("You win!")

print("Thank you for playing!")
input("Press enter to exit the game...")
