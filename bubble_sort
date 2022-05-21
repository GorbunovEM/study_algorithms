n = map(int, input())
lst = [i for i in n]

for i in range(0, len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            swap = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = swap
print(lst)
