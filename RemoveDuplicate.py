Numbers = [1, 5, 7, 9, 3, 5, 7, 6, 0, 5]

for Number in Numbers:
    if Numbers.count(Number) > 1:
        Numbers.remove(Number)
print(Numbers)
