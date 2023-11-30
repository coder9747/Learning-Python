class Person:
    pay_rate = 0.9
    arr = []
    def __init__(self,name:str,age:int):
        assert age>=0,"Age Cannot Be Negative";
        self.name = name
        self.age = age
        Person.arr.append(self);
    
    def getName(self):
        return self.name;
    def getAge(self):
        return self.age;
    def getHeight(self):
        return self.height;