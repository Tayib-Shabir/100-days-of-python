# Day3 Project: Treasure Island Game
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_route = input('You are at the cross road. Where do you want to go? Type "left" or "right"\n').lower()
if first_route == "left":
    second_route = input('you have come to an lake. '
                         'There is an island in the middle of the lake. '
                         'Type "wait" to wait for the boat or type "swim" to swim across\n').lower()
    if second_route == "wait":
        third_route = input("You arrive at the island unharmed. "
                            "There is a house with 3 doors. One red, one yellow and one blue. "
                            "Which colour do you choose?\n").lower()
        if third_route == "yellow":
            print("You found the treasure and won!")
        elif third_route == "blue":
            print("You enter a room of beasts. Game Over.")
        elif third_route == "red":
            print("The Room is full of  Fire. Game Over. ")
        else:
            print("You chose the door that doesn't exist. Game Over.")
    elif second_route == "swim":
        print("You got attacked by an angry Sea King. Game Over.")

elif first_route == "right":
    print("you fell into a hole. Game Over.")