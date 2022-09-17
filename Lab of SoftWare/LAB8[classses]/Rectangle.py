"""author = "GARRY GY"
Date:2021-10-19
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class Rectangle(object):

    def __init__(self,width=10,height=10):
        self.__height = height
        self.__width = width

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __str__(self):
        return str(self.__width) + " x " + str(self.__height)

    def __repr__(self):
        return "Rectangle(%d, %d)"%(self.__width,self.__height)

    def get_area(self):
        return self.__height * self.__width

    def get_perimeter(self):
        return 2*(self.__width + self.__height)

# r1 = Rectangle(3, 4)
r2 = Rectangle()
print(r2.get_width(), r2.get_height())
print(r2.__repr__())
print(r2.__str__())