 # firstly import the random module.
import random 
print("Welcome to the Rock, Paper, Scissors Mini version")
# creating an input function(with the variable name player) to hold the gamers input.
replay= True
while replay :
    player =(input("What would you choose: 'r' is for rock', 'p' is for paper', 's' is for scissors' \n ")).lower()
    
#first Validation
    if (player != 'p'  and player != 'r' and player != 's'):
            print("Invalid Entry,Try again.")
            break
            
    player_list=["rock","paper","scissors"]
    
    if player == 'r':
        game_player = 'rock'
    elif player == 'p':
        game_player = 'paper'
    else :
        game_player = 'scissors'
    # now creating the random function for the computer to be able to pick a random number.
    computer_choice = random.choice(player_list)
    print(f"player({game_player}) : computer({computer_choice})")
    
    # Now creating the logic or the rules to follow for the rock,paper,scissors game
    if game_player == 'rock' and computer_choice == 'scissors':
        print("You win")
    elif computer_choice == 'rock' and game_player == 'scissors':
        print("Computer Wins,You Lose!")
    elif computer_choice =='rock' and game_player == 'paper':
        print("You win")
    elif computer_choice == 'paper'and  game_player == 'rock':
        print("Computer Wins,You Lose")
    elif computer_choice == 'paper' and game_player == 'scissors':
        print("You Win")
    elif computer_choice == 'scissors' and game_player == 'paper':
        print(" Computer Wins,You Lose")
    elif game_player == 'rock' and computer_choice == 'paper':
        print(" Computer Wins,You Lose")
    elif game_player == 'paper' and computer_choice == 'scissors':
        print(" Computer Wins,You Lose")
    elif game_player == computer_choice:
        print("Draw")
        continue    
    continue_game = input("would you like to continue playing,Enter('y' for yes).lower() or ('n' for No).").lower()
    if continue_game == 'y':
        replay =True
    else:
        replay = False
        print("Thank you for playing.")
