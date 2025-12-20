import random
options=("rock","paper","scissors")
user=input("Enter Your name: ")
running=True
while running:
    player=None
    computer=random.choice(options)
    
    while player not in options:
        player=input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a TIE !!!")
    elif player=="rock" and computer=="scissors":
        print(f"{user} WINS !")
    elif player=="paper" and computer=="rock":
        print(f"{user} WINS !")
    elif player=="scissors" and computer=="paper":
        print(f"{user} WINS !")
    else:
        print(f"Computer wins against {user} :(")


    if not input("Play Again? (y/n): ").lower()=="y":
        running=False

print("Thanks for playing!!")


