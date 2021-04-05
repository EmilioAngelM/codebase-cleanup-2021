
from random import choice

valid_options = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    Params:
        choice1 and choice2 are both string: one of "Rock", "Paper", or "Scissors"
    """
    winners = {
        "rock":{
            "rock": None, # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, # represents a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, # represents a tie
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice




if __name__ == "__main__":
#
# USER SELECTION
#
    
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_options)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    #if u == "rock" and c == "rock":
    #    print("It's a tie!")
    #elif u == "rock" and c == "paper":
    #    print("The computer wins")
    #elif u == "rock" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "paper" and c == "rock":
    #    print("The computer wins")
    #elif u == "paper" and c == "paper":
    #    print("It's a tie!")
    #elif u == "paper" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "scissors" and c == "rock":
    #    print("The computer wins")
    #elif u == "scissors" and c == "paper":
    #    print("The user wins")
    #elif u == "scissors" and c == "scissors":
    #    print("It's a tie!")

    #if u == "rock":
    #    if c == "rock":
    #        print("It is a tie!")
    #    elif c == "paper":
    #        print("Oh, better luck next time. The computer won")
    #    elif c == "scissors":
    #        print("Great Job! You WON")
    #elif u == "paper":
    #    if c == "rock":
    #        print("Great Job! You WON")
    #    elif c == "paper":
    #        print("It is a tie!")
    #    elif c == "scissors":
    #        print("Oh, better luck next time. The computer won")
    #elif u == "scissors":
    #    if c == "rock":
    #        print("Oh, better luck next time. The computer won")
    #    elif c == "paper":
    #        print("Great Job! You WON")
    #    elif c == "scissors":
    #        print("It is a tie!")

    winner = determine_winner(u,c)

    if winner == u:
        print("Great Job! You WON")
    elif winner ==c:
        print("Oh, better luck next time. The computer won")
    elif winner == None:
        print("It is a tie!")