"""author = "GARRY GY"
Date:2021-11-25
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class Stack:
    def __init__(self):
        self.__items = []
    def is_empty(self):
        return self.__items == []
    def push(self, item):
        self.__items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError('The stack is empty!')
        return self.__items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError('The stack is empty!')
        return self.__items[len(self.__items) - 1]
    def size(self):
        return len(self.__items)
    def __str__(self):
        return 'Stack: ' + str(self.__items)

def starts(my_string,index):
    while my_string[index] != "(" and index < len(my_string) -1:
        index += 1
    else:
        start = True
    return start,index

def longest_valid_brackets(my_string):
    if my_string != "":
        start,index = starts(my_string,0)
    else:
        return -1
    S = Stack()
    count = 0
    br = 0
    max_co = []
    for x in range(len(my_string)):
        if my_string[x] != ")" and start == True and x >= index:
            S.push(my_string[x])
        elif my_string[x] == ")":
            br += 1
            if S.is_empty() == True:
                return -1 if max_co == [] else max(max_co)
            else:
                while S.pop() != "(":
                        count += 1
                else:
                    br += 1
                    if S.is_empty() == False and len(my_string)-1 != x:
                        continue
                    else:
                        max_co.append(count+br-2)
                        count = 0
                        br = 0
                        if len(my_string)-1 != x:
                            start,index = starts(my_string,x)
                        if x == len(my_string)-1:
                            return max(max_co)

    return -1 if max_co == [] else max(max_co)


print(longest_valid_brackets("(abc)(defg)"))
print(longest_valid_brackets("()"))
print(longest_valid_brackets("a(bc(de(fg)hi)jklm)"))
print(longest_valid_brackets(")abc("))
print(longest_valid_brackets("op(qrst(uvwxyz)"))
print(longest_valid_brackets("(abc)"))
print(longest_valid_brackets("abcd"))
print(longest_valid_brackets("((((()))))"))
print(longest_valid_brackets(""))
print(longest_valid_brackets("((abc)(defg))"))
print(longest_valid_brackets("a(b(i)m)sd(c(c))"))