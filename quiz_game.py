question=("Which planet is known as the Red Planet?",
          "What is the capital city of Japan?",
          "What is the primary gas that makes up the air we breathe?",
          "The Eiffel Tower is located in which European city?",
          "Who wrote the play Romeo and Juliet?")
option=(("A) Venus","B) Mars","C) Jupiter","D) Saturn"),
        ("A) Seoul","B) Beijing","C) Bangkok","D) Tokyo"),
        ("A) Oxygen","B) Carbon Dioxide","C) Nitrogen","D) Hydrogen"),
        ("A) Rome","B) London","C) Paris","D) Berlin"),
        ("A) Charles Dickens","B) William Shakespeare","C) Jane Austen","D) Mark Twain")
         )
answer=("B","D","C","C","B")
guesses=[]
score=0
que_num=0

for que in question:
    print("*********************************")
    print(que)
    for opt in option[que_num]:
        print(opt)
    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answer[que_num]:
        score+=1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
        print(f"{answer[que_num]} is the correct answer")
    que_num+=1

print("*********    RESULTS     *********")
print("Answers: ",end="")
for ans in answer:
    print(ans,end=" ")
print()
print("Your answer: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(question)*100)
print(f"Your score is: {score}%")

