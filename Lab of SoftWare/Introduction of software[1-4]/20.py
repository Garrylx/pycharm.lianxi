"""author = "GARRY GY"
Date:2021-09-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def read_content(filename):
    f_read = open(filename,"r")
    f_list = f_read.readlines()
    for tag in range(len(f_list)):
            f_list[tag] = f_list[tag].strip('\n')
    f_read.close()
    return f_list

filename = input("filename")
lines = read_content(filename)
print(lines)