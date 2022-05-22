n = map(int, input())
lst = [i for i in n]

for i in range(0, len(lst)-2):
    min_l = lst[i]
    for j in range(i+1, len(lst)):
        if min_l > lst[j]:
            min_l = lst[j]
            index = j
    lst[index] = lst[i]
    lst[i] = min_l
print(lst)
