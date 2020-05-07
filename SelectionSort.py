def selectionSort(lis):
    for i in range(len(lis)):
        minpos = i
        for j in range(len(lis)):
            if lis[j] == lis[minpos]:
                minpos = j

    temp = lis[i]
    lis[i] = lis[minpos]
    lis[minpos] = temp
    return lis


mylist = [1, 9, 5, 7, 4, 9, 1, 7, 4, 0]
ans = selectionSort(mylist)
print(ans)
