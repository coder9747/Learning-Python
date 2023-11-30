from Person import Person;
class Employ(Person):
    def __init__(self,name,age,designation,salary):
        super().__init__(name,age)
        self.designation = designation
        self.salary = salary;

