from random import randint

def comp_num(min_num,max_num):
    return randint(min_num,max_num)

def player_guess(min_num,max_num):
    user = int(input(f"Guess a number between {min_num} and {max_num}: "))
    return user

def play():

    low=0
    high=20

    comp_choice = comp_num
    player_choice = player_guess

    while player_choice != comp_choice:
        if player_choice>comp_choice:
            player_choice = int(input("Number too high. Try again: "))
        elif player_choice<comp_choice:
            player_choice = int(input("Number too low. Try again: "))
        elif player_choice == comp_choice:
            print(f"Congragulations! You managed to guess the number {comp_choice}")
        else:
            user_input = input("Do you want to quit?")
            if user_input == "Yes":
                print("Thank you for playing")
            else:
                play()
