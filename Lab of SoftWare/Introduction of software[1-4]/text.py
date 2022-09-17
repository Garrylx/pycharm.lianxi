# import requests
# url = "http://interface.debate.cool/onlycode"
# data = {"mycode":"gy","command":"read"}
# res = requests.post(url = url,data = data)
# print(res.text)
#
# url = "http://interface.debate.cool/onlycode"
# s = "x"
# data = {"data":s,"mycode":"gy","command":"read"}
# res = requests.post(url = url,data = data)
# print(res.text)
#
# def rate(n):
#     total = 0
#     i = 0
#     k = 4
#     while i < 4:
#         j = 0
#         k += 4
#         while j < i:
#             k += 3
#             total += j
#             j += 1
#         i += 1
#     return k
# print(rate(2))

# letters = ['a', 'c', 'f', 'b', 'g']
# shifting(letters, 3)
# print(letters)
# ['a', 'c', 'c', 'f', 'g']

def insertion_row(data):
    for i in range(1,len(data)):
        item_to_insert = data[i]
        j = i - 1
        while j >= 0 and data[j] > item_to_insert:
                data[j+1] = data[j]
                j -= 1
        data[j+1] = item_to_insert

    return data
print(insertion_row(['x', 'b', 'f', 'u', 'r', 'k']))
