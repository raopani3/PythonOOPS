def printSQRT():
    num = 1
    while num <= 10:
        sq = num * num
        yield sq
        num += 1


val = printSQRT()

for i in val:
    print(i)
