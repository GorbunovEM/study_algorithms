n = map(int, input())
lst = [i for i in n]

for i, l in enumerate(lst):
    j = i - 1
    while (j >= 0) and (l < lst[j]):
        lst[j+1] = lst[j]
        j = j - 1
    lst[j+1] = l
print(lst)
