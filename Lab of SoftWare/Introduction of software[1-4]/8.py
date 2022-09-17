"""author = "GARRY GY"
Date:2021-09-17
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

elist = []
num_input = int(input("Enter number of rows: "))

def basic_form(elist):
    elist = []
    for i in range(num_input):
        if i != 0 and i != num_input-1:
            elist.append(" ")
        else:
            elist.append("*")
    return elist
empty_list = basic_form(elist)
# print(empty_list)
def finall_form(empty_list,num_input):
    for x in range(3):
        if x == 0 or x == 2:
            print("*"*num_input)
        else:
            symbols = (num_input - 1) // 2
            y = 1
            for times in range(symbols):
                while y < num_input - 1:

                    if y < symbols:
                        empty_list[y] = "*"
                        empty_list[-(y+1)] = "*"
                        for item in empty_list:
                            print(item,end="")
                        print("")
                        empty_list = basic_form(elist)
                        y += 1
                    elif y == symbols:
                        empty_list[y] = "*"
                        for item in empty_list:
                            print(item,end="")
                        empty_list = basic_form(elist)
                        print("")
                        y += 1
                    elif y > symbols:
                        empty_list[y] = "*"
                        empty_list[-(y+1)] = "*"
                        for item in empty_list:
                            print(item,end="")
                        empty_list = basic_form(elist)
                        print("")
                        y += 1
                    else:
                        print("Bad cases happened!")


finall_form(empty_list,num_input)