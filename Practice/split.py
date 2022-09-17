"""author = "GARRY GY"
Date:2021-04-02

"""
def split_str(str1,list1):
    for item in str1:
        list1.append(item)
    return list1,str1

def sum_num(list1):
    num1 = 0
    for num in list1:
        num1 += int(num)
    return num1

str1 = input("type a number")
list1 = []
while len(list1) != 1:
    split_str(str1,list1)
    num1 = sum_num(list1)
    if len(list1) == 1:
        break
    str1 = str(num1)
    list1 = []


print(int(list1[0]))






