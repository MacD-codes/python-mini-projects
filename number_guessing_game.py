import random

low=1
high=100
answer=random.randint(low,high)
print(answer)
guesses=0
is_running=True

print("((*((*))*    Number Guessing Game    *((*))*))")
print("\nSelect a Number between 1 to 100")

while is_running:
    guess=input("\nEnter a number to guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess<low or guess>high:
            print("Your guess is out of range!!")
            print("Select a Number between 1 to 100")
        elif guess<answer:
            print("Too low! Go higher ...")
        elif guess>answer:
            print("Too high! Go lower ...")
        else:
            print("Your Guess is correct!!")
            print("The answer was",answer)
            print(f"Number of guesses: {guesses}")
            is_running=False
    else:
        print("Invalid guess!!") 
        print("Select a Number between 1 to 100")