"""author = "GARRY GY"
Date:2021-08-02
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

import threading

lists = []

def add_num():
	for u in range(5):
	    lists.append(u)
	    print("add",u)

def read_num():
    print(lists)

if __name__ == "__main__":
    fd = threading.Thread(target=add_num())
    fd.start()
    fg = threading.Thread(target=read_num())
    fg.start()