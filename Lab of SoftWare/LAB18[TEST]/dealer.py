"""author = "GARRY GY"
Date:2021-11-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class Car(object):

    def __init__(self,make, model, year,price=10000):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__price = price

    def __str__(self):
        return "{} {} {}, ${}".format(self.__year,self.__make,self.__model,self.__price)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def set_price(self,price):
        if price >= 0:
            self.__price = price

class Dealership(object):

    def __init__(self,name):
        self.__name = name
        self.__stock = []

    def get_name(self):
        return self.__name

    def add_car(self,car):
        if not isinstance(car,Car):
            raise ValueError("This dealership only sells cars!")
        else:
            self.__stock.append(car)

    def total_value_of_stock(self):
        total = 0
        for car in self.__stock:
            total += car.get_price()
        return total
