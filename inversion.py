lst = [3,2,1]

def naive_inv(lst):
    
    inv: int = 0
    for i in range(0,len(lst)-1):
        n = i + 1
        for j in range(n,len(lst)):
            if lst[i] > lst[j]:
                inv = inv + 1
    return inv



def merge_sort_inv(lst):
    if len(lst) < 2:
        return lst, 0
    else:
        mid = len(lst) // 2
        lft, inv_lft = merge_sort_inv(lst[:mid])
        rgt, inv_rgt = merge_sort_inv(lst[mid:])

    res = []
    inv = 0 + inv_lft + inv_rgt
    i, j = 0, 0

    while i < len(lft) and j < len(rgt):
        if lft[i] <= rgt[j]:
            res.append(lft[i])
            i += 1
        else:
            res.append(rgt[j])
            j += 1
            inv += (len(lft)-i)

    while i < len(lft):
        res.append(lft[i])
        i += 1

    while j < len(rgt):
        res.append(rgt[j])
        j += 1

    return res, inv
