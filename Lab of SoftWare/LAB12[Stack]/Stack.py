"""author = "GARRY GY"
Date:2021-11-03
"""
class IndexError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "ERROR: The stack is empty!"


class Stack:
    from copy import deepcopy

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items == []:
            raise IndexError
        return self.__items.pop()

    def peek(self):
        if self.__items == []:
            raise IndexError
        return self.__items[len(self.__items) - 1]

    def __str__(self):
        return "Stack: {}".format(self.__items)

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def push_list(self, a_list):
        self.__items += a_list

    def multi_pop(self, number):
        if len(self.__items) >= number:
            for x in range(number):
                self.__items.pop()
            return True
        else:
            return False

    def copy(self):
        newone = Stack()
        newone.push_list(self.__items)
        return newone

    def __eq__(self, other):
        res = True
        if isinstance(other,Stack) == True:
            if len(self.__items) == len(other.__items):
                for x in range(len(self.__items)):
                    if self.__items[x] == other.__items[x]:
                        res = True
                    else:
                        res = False
                if res == True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

def reverse_sentence(sentence):
    k = Stack()
    k.push_list([x for x in sentence])
    str_reverse = []
    str_final = ""
    for num in range(len(sentence)):
        comp = k.pop()
        if comp != " " and comp != "":
            str_reverse.append(comp)
        else:
            str_reverse = str_reverse[::-1]
            str_final = str_final + "".join(str_reverse) + comp
            str_reverse =[]
    str_reverse = str_reverse[::-1]
    str_final = str_final + "".join(str_reverse)
    return str_final.strip()

def balanced_brackets(text):
    ex_stack = Stack()
    for item in text:
        ex_stack.push(item)
    right_bracket_list = []
    left_bracket_list = []
    do = False
    for time in range(len(text)):
            do = False
            tmp = ex_stack.pop()
            if tmp in [")",">"]:
                right_bracket_list.append(tmp)
            if tmp in ["(","<"] and right_bracket_list != []:
                left_bracket_list.append(tmp)
                if tmp == "(" and right_bracket_list.pop() == ")":
                    left_bracket_list.pop()
                    do = True
                    pass
                elif tmp == "<" and right_bracket_list.pop() == ">":
                    left_bracket_list.pop()
                    do = True
                    pass
                else:
                    return False
            if tmp in ["(", "<"] and right_bracket_list == [] and do ==False:
                left_bracket_list.append(tmp)
    if left_bracket_list != [] or right_bracket_list != []:
        return False
    else:
        return True



#
# postfix_stack = Stack()
# postfix_stack.push(3)
# postfix_stack.push(4)
# x = postfix_stack.pop() * postfix_stack.pop()
# postfix_stack.push(x)
# postfix_stack.push(6)
# x = 1/(postfix_stack.pop() / postfix_stack.pop())
# postfix_stack.push(x)
# postfix_stack.push(3)
# x = postfix_stack.pop() + postfix_stack.pop()
# postfix_stack.push(x)
# print(postfix_stack.pop())

def compute(num1,num2,ope):
    if ope == '/':
        return int(num2) // int(num1)
    elif ope == "^":
        return int(num2)**int(num1)
    else:
        return str(eval(str(num2) + str(ope) + str(num1)))

def evaluate_postfix(postfix_list):
    postfix_stack = Stack()
    num = 0
    for x in postfix_list:
        if x not in ["+","-","*","/","%","^"]:
            postfix_stack.push(x)
        else:
            res = compute(postfix_stack.pop(),postfix_stack.pop(),x)
            postfix_stack.push(res)
    return postfix_stack.pop()

print(evaluate_postfix(['2', '4', '3', '*', '^']))




