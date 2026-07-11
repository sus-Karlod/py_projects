import random

def game():
    player_choice = input("Enter a choice ( rock, paper, scissors ) : ").lower()

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Its a tie"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock, You lose."
        else :
            return "Rock smashes scissors, You win!"
        
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock, You win!"
        else :
            return "Scissors cut paper, You lose."
        
    elif player == "scissors":
        if computer == "rock":
            return "Rock beats scissors, You lose."
        else :
            return "Scissors cut paper, You win!"
    
choices = game()
result = check_win(choices["player"],choices["computer"])
print(result)
