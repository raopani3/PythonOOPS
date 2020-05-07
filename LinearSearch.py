pos = -1


def search(lis, n):
    number = n

    for i in range(len(lis)):

        if lis[i] == number:
            globals()['pos'] = i
            return True


ls = [10, 2, 4, 3, 9, 4, 6, 6, 9, 10]

ans = search(ls, 6)
print(ans)

if ans:
    print("Found at {}".format(pos))
else:
    print("Not found")
