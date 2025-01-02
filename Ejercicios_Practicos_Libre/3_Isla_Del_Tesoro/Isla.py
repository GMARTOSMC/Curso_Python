# .lower() para convertir la salida del input a minúscula

print ("Welcome to Treasure Island.")
print("Made by Gonzalo Martos Conesa")
print ("You're at a cross road. Where do you want to go?")
road = input('Type "left" or "right": ').lower()

if road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.") 
    lake = input('Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
    if lake == "wait":
        print("You arrive at the island unarmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue. Which colour do you choose?")
        door = input('Type "red", "yellow" or "blue": ').lower()
        if door == "red":
            print("You are burned by fire.")
            print("Game Over")
        elif door == "blue":
            print("You are eaten by a tiger.")
            print("Game Over")
        elif door == "yellow":
            print("You win!")
            print("Congratulations") 
        else:
            print("Game Over")     
    else:
        print("You are attacked by a shark.")
        print("Game Over")
else:
    print("You Fall into a Hole.")
    print("Game Over")