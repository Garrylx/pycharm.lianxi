"""Author = GARKAX GY
Date: 2022--16
TIME FLIES!
"""
"""author = "GARRY GY"
Date:2021-11-05
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, a=None):
        self.head = Node(None)  # a dummy head node
        if a:
            for data in a:
                self.insert(data, pos=len(self))  # append nodes to the end

    def __len__(self):
        cur_node = self.head.next
        count = 0
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    def __repr__(self):
        rep = ''
        cur_node = self.head.next
        while cur_node:
            rep += str(cur_node) + ', '
            cur_node = cur_node.next
        if len(rep) > 0:
            rep = rep[:-2]
        return '[' + rep + ']'

    def insert(self, data, pos=0):  # insert data at position pos
        n = self.head
        for i in range(pos):
            n = n.next
        next_n = n.next
        current_n = Node(data)
        current_n.next = next_n
        n.next = current_n



    def delete(self, pos):  # delete the node at position pos
        n = self.head
        for i in range(pos-1):
             n = n.next
        n.next = n.next.next


def check_and_insert(lst, unsorted_lst):
    unsorted_data = unsorted_lst.data
    sorted_lst = lst.head
    index_s = 0
    while sorted_lst != unsorted_lst:
        if unsorted_data <= sorted_lst.next.data:
            lst.insert(unsorted_data,index_s)
            break
        else:
            sorted_lst = sorted_lst.next
            index_s += 1
    else:
        lst.insert(unsorted_data,index_s)

def insert_sort_linkedlist(a):
    unsorted_lst = a.head.next.next
    unsorted_num = 3
    while(unsorted_lst.next != None):
        check_and_insert(a, unsorted_lst)
        unsorted_lst = unsorted_lst.next
        a.delete(unsorted_num)
        print(a)
        unsorted_num += 1
    else:
        check_and_insert(a, unsorted_lst)
        a.delete(unsorted_num)
        print(a)

# x = LinkedList([1])
# print(len(x))

a = LinkedList([87, 61, 3, 89, 98, 65, 15, 60, 21, 36])
insert_sort_linkedlist(a)


















