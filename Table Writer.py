Number = input("Enter Number Of Which You Want The Table : ")
Two = int(Number) * 2
Three = int(Number) * 3
Four = int(Number) * 4
Five = int(Number) * 5
Six = int(Number) * 6
Seven = int(Number) * 7
Eight = int(Number) * 8
Nine = int(Number) * 9
Ten = int(Number) * 10
while True:
    if "-" in Number or Number == 0:
        print("Only Type Natural Numbers")
        break
    else:
        print(Number, "X 1 =", Number)
        print(Number, "X 2 =", Two)
        print(Number, "X 3 =", Three)
        print(Number, "X 4 =", Four)
        print(Number, "X 5 =", Five)
        print(Number, "X 6 =", Six)
        print(Number, "X 7 =", Seven)
        print(Number, "X 8 =", Eight)
        print(Number, "X 9 =", Nine)
        print(Number, "X 10 =", Ten)
        break
