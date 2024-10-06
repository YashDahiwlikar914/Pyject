import math

Root = int(input("Enter A Perfect Square Number : "))
Answer = math.sqrt(Root)
ConvertedAnswer = int(Answer)

print("Type Yes Or No")
Question = input("Do You Want To Guess The Answer? - ").lower()
No = "no"
Yes = "yes"
if Question == No:
    print(int(Answer))
else:
    Guess = int(input("Type Your Answer : "))
if Question == Yes:
    if Guess == ConvertedAnswer:
        print("Your Answer Is Correct!")
        print(int(Answer))
    else:
        print("Your Answer Is Wrong!","Correct Answer Is",ConvertedAnswer)

