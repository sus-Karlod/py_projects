import random

class RPS():
    def __init__(self):
        self.score = {"player": 0, "computer": 0}

    def get_player_choice(self):
        player_choice = input("Enter your choice(rock, paper, scissor) : ").lower()
        return player_choice

    def get_computer_choice(self):
        options = ["rock", "paper", "scissor"]
        computer_choice = random.choice(options)
        return computer_choice

    def determine_winner(self, player, computer):
        if player == computer:
            return("It's a tie")
        elif player == "rock":
            if computer == "scissor":
                self.score["player"] += 1
                return("Rock beats scissor, You win!")
            else:
                self.score["computer"] += 1
                return("Paper covers rock, You lose...")
        elif player == "paper":
            if computer == "rock":
                self.score["player"] += 1
                return("Paper covers rock, You win!")
            else:
                self.score["computer"] += 1
                return("Scissor cuts paper, You lose...")
        elif player == "scissor":
            if computer == "paper":
                self.score["player"] += 1
                return("Scissor cuts paper, You win!")
            else:
                self.score["computer"] += 1
                return("Rock beats scissor, You lose...")
         
    def play_round(self):
        player = self.get_player_choice()
        computer = self.get_computer_choice()
        result = self.determine_winner(player, computer)
        print(result)
        print(f"Score - You : {self.score['player']}, Computer : {self.score['computer']}")

game = RPS()

while True:

    game.play_round()

    if game.score['player'] == 3:
        print("You win the game")
        again = input("Do you want to play again? (yes/no) : ").lower()
        if again != "yes":
            print("Thanks for playing the game")
            break
        else:
            game = RPS()
    
    elif game.score['computer'] == 3:
        print("Computer wins the game")

        again = input("Do you want to play again? (yes/no) : ").lower()
        if again != "yes":
            print("Thanks for playing the game")
            break
        else:
            game = RPS()
    