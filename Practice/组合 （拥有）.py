class Dog:
    def __init__(self,name,breed,owner,ownergender):
        self.name = name
        self.breed = breed#品种
        self.owner = owner
        self.ownergender = ownergender


class Person:
    def __init__(self,name,gender):
        self.name =  name
        self.gender = gender

nick = Person('Garry',"female")
stan = Dog("stan","Bulldog",nick,"female")
print(stan.owner.name)
mick = Person("Garry","male")
span = Dog("span","Bulldog",nick,mick)
print(span.ownergender.gender)