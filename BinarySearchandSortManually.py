pos = -1


def sort(lis):
    length = len(lis)
    for i in range(length):
        for j in range(0, length - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


def binarySearch(searchList, numbertosearch):
    lower = 0
    upper = len(searchList)

    n = numbertosearch

    for i in range(len(searchList)):
        mid = (lower + upper) // 2
        if searchList[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if searchList[mid] < n:
                lower = mid
            else:
                upper = mid


mylist = [1, 9, 5, 7, 4, 9, 1, 7, 4, 0]
orderedList = sort(mylist)
print(orderedList)

ans = binarySearch(orderedList, 100)


if ans:
    print("Number found at {} position".format(pos))

else:
    print("Not found")
