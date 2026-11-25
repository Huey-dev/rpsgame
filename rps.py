import random

while True:
    user_option = input(
        "Choose your option between \n 1. Rock\n 2. Paper\n 3. Scissor \n \5"
    )
    
    user_input = int(user_option)
    if user_input >= 1 and user_input <= 3:
        break
    print("Invalid! Choose your option between \n 1. Rock\n 2. Paper\n 3. Scissor \n")


choices_list = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(choices_list)

user_choice = choices_list[user_input - 1]
print(f"You chose {user_choice}")
print(f"Computer chose {computer_choice}")
