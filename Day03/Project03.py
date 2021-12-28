print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

answer = input("You're at a cross road. Where do you want to go? Type 'left' ar 'right'")
answer = answer.lower()
if answer == "left":
    answer = input("You cone to a Lake. There is an island in the middle of the Lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    answer = answer.lower()
    if answer == "wait":
        answer = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        answer = answer.lower()
        if answer == "red":
            print("Burned by fire.GAME OVER.")
        elif answer == "blue":
            print("Eaten by beats. GAME OVER")
        elif answer == "yellow":
            print("YOU WIN !!!!")
        else:
            print("GAME OVER !!!")
    else:
        print("You was attacked by a shark. GAME OVER.")
else:
    print("You fall into a hole. GAME OVER.")
