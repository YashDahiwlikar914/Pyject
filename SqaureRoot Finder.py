import math

Root = int(input("Enter A Perfect Square Number : "))
Answer = math.sqrt(Root)
ConvertedAnswer = int(Answer)
while True:
    print("Type Yes Or No")
    Question = input("Do You Want To Guess The Answer? - ").lower()
    if "yes" in Question or "no" in Question or "ok" in Question:
        if "no" in Question:
            print("Square Root Of", Root, "=", int(Answer))
            break
        else:
            Guess = int(input("Type Your Answer : "))
            if Guess == ConvertedAnswer:
                print("Your Answer Is Correct!", "It's", int(Answer))
                break
            else:
                print("Your Answer Is Wrong!", "Correct Answer Is", ConvertedAnswer)
                break
    else:
        print("Type Yes Or No Only!")
