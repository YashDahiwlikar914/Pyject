Number = int(input("Print Till How Many Numbers? - "))
Times = Number + 1
while True:
    for i in range(Times):
        if 0 != i:
            print(i)
        print(end=" ")
    Ans = input("Wanna Continue? (Y/N) : ")
    if Ans == 'N':
        break
