"""Author = GARKAX GY
Date: 2022--19
TIME FLIES!
"""


# Alpha is list of jobs, which are presented by time intervals.
def job_selection(a):
    start_lst = []
    end_lst = []
    # 二维结束列表【出现一个开头对应多个结束的情况】
    n = len(a)
    # 每一组点开头和结尾对应的数组索引是相同的，开始列表和结束 列表长度一致
    for i in range(n):
        if a[i][0] not in start_lst:
            start_lst.append(a[i][0])
            end_lst.append([a[i][1]])
        else:
            # 如果有出现相同开头的元素，就把结束点加到对应索引的结束列表的位置
            ind = start_lst.index(a[i][0])
            end_lst[ind] = end_lst[ind] + [a[i][1]]
    find = 0
    sta_len = len(start_lst)
    final_lst = []

    while find <= sta_len:
        start_ele = start_lst[find]
        end_ele = max(end_lst[find])
        final_lst.append((start_ele, end_ele))
        if end_ele in start_lst:
            # 这一次的结尾是下一次的开头
            find = start_lst.index(end_ele)
        else:
            return final_lst


x = [(1, 4), (3, 5), (1, 3), (4, 6), (5, 7), (6, 9)]
print(job_selection(x))
