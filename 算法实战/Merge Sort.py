"""Author = GARKAX GY
Date: 2022--17
TIME FLIES!
"""


def merge(lst, l ,m, r):
    tmp = [0] * (r - l + 1)
    tmp_ind = 0
    r_start = m+1
    l_start = l
    while(l_start <= m and r_start <= r):
        if(lst[l_start] > lst[r_start]):
            tmp[tmp_ind] = lst[r_start]
            r_start += 1
        else:
            tmp[tmp_ind] = lst[l_start]
            l_start += 1
        tmp_ind += 1
    if l_start > m:
        for x in lst[r_start:r+1]:
            tmp[tmp_ind] = x
            tmp_ind += 1
    else:
        for x in lst[l_start:m+1]:
            tmp[tmp_ind] = x
            tmp_ind += 1
    for x in range(r, l-1, -1): # 归并后的有序数组替换原数组中相同位置的元素
        lst[x] = tmp.pop()


def merge_sort(a, l, r):
    if l != r:
        merge_sort(a, (l+r)//2+1, r)
        merge_sort(a, l, (l + r) // 2)
        merge(a, l, (l+r)//2, r)

a = [87, 61, 3, 89, 98, 65, 15, 60, 21, 36]
merge_sort(a,0,9)
print(a)


