"""author = "GARRY GY"
Date:2021-01-24

"""
class Dog():
    # __init__
    def __init__(self,name,color,distance):
        self.name = name
        self.color = color
        self.distance = 0#添加默认值

    def sit(self):
        print("我做下来了")

    def roll(self):
        print("done")

#类的创建实例
dog1 = Dog("xiaohei","white",0)
dog2 = Dog("xiaobai","black",0)

print(dog1.sit())
print(dog2.roll())

#类的继承
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+"eating")

    def sleep(self):
        print(self.name+"sleeping")

class Teacher(Person):
    def __init__(self,name,age,title):
        super().__init__(name,age)#调用父类里面的初始化方法，构造方法 但不写也行
        self.title = title

    #重写方法

    def eat(self):
        print(self.name+"eating at canteen")




person1 = Teacher("kaka","19","kai")
person1.eat()


"""author = "GARRY GY"
Date:2021-01-24

"""
class Person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personinfo(self):
        print(self.name,self.age,self.gender)

class Student(Person):
    def __init__(self,name,age,gender,collage,cls):
        super().__init__(name,age,gender)#super为父类
        self.collage = collage
        self.cls = cls

    def personinfo(self):
        super().personinfo()
        print(self.collage,self.cls)

    def study(self,Teacher):
        Teacher.tea_obj()
        print("我学会了"+Teacher.name)

s = Student("wangwei",19,"man","daxue","4")
s.personinfo()

class Teacher(Person):
    def __init__(self,name,age,gender,collage,profession):
        super().__init__(name,age,gender)
        self.collage = collage
        self.profession = profession

    def __str__(self):
        return self.name + str(self.age) + self.gender#修改str方法以后可以直接打印相关信息

    def tea_obj(self):
        print("今天教了头发护理")

t = Teacher("xw",19,"man","dkwmd","barber")


s.study(t)
print(t)#直接打印  否则会打印地址

