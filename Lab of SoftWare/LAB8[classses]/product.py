"""author = "GARRY GY"
Date:2021-10-20
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class Product(object):

    def __init__(self,product_id,product_name,product_price=1):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        return self.__product_name + "(id = %s), " % self.__product_id + "$%d"%self.__product_price

    def set_product_price(self,product_price):
        if product_price >= 0:
            self.__product_price = product_price
        else:
            pass

    def get_product_price(self):
        return self.__product_price

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name

    def set_product_id(self, product_id):
        if product_id > 0:
            self.__product_id = product_id
        else:
            pass

    def get_product_id(self):
        return self.__product_id
