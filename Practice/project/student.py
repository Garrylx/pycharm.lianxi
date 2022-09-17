"""author = "GARRY GY"
Date:2021-07-08
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class Student(object):
    def __init__(self,name,gender,age,tel):
        self.name = name
        self.gender = gender
        self.age = age
        self.tel = tel

    def __str__(self):
        return f"""
        The student's name is {self.name}
        ,gender is {self.gender},
        {self.age} years old,
        telephone number is {self.tel}
        """


