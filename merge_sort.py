def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst) // 2
        lft = merge_sort(lst[:mid])
        rgt = merge_sort(lst[mid:])

    res = []
    i, j = 0, 0

    while i < len(lft) and j < len(rgt):
        if lft[i] < rgt[j]:
            res.append(lft[i])
            i += 1
        else:
            res.append(rgt[j])
            j += 1

    while i < len(lft):
        res.append(lft[i])
        i += 1

    while j < len(rgt):
        res.append(rgt[j])
        j += 1

    return res
