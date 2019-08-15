def heap_insert(a: List[int], k):
    a.append(k)
    i = len(a) - 1
    p = (i-1)//2
    while p > -1 and a[p] < a[i]:
        a[p], a[i] = a[i], a[p]
        i = (i-1) // 2
        p = (i-1) // 2
