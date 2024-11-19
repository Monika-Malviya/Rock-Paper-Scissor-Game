"""
WORKFLOW OF PROJECT:
1) Input from user(Rock, Paper, scissor )
2) Computer choice(Computer will chioose randomly not conditionally)
3) Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B - Paper
Paper - paper = tie
Paper - Rock = Paper win
Paper - scissor = scissor win

C - scissor
scissor - scissor = tie
scissor - Rock = Rock win
scissor - Paper = scissor win
"""

import random
item_list= ["Rock","Paper","Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same : Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes scissor = you win") 

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper cover Rock = you win ")
    else:
        print("Scissor cuts Paper = Compuer win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes scissor = Computer win")
    else:
        print("Scissor cuts paper = you win")  

print("End the Game ") 
                                       