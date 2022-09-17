"""author = "GARRY GY"
Date:2020-11-21-
"""
class Shape():
    def __init__(self,w,f):
        self.non = w
        self.mom = f
    def print_size(self):
        print("""{}by{}
        """.format(self.non,self.mom))

"""class Square(Shape):
    pass"""

class Square(Shape):#继承
    def area(self):
        return self.non * self.mom

    def print_size(self):
        print("""{}  {}
        """.format(self.non,self.mom))#覆盖

b_square = Square(20,90)
print(b_square.area())


a_square = Square(20,20)
a_square.print_size()
