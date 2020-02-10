class Person:
    def __init__(self):
        self.Name = str()
        self.Age = int()        

    def getInput(self):
        self.Name = input('Name : ')
        self.Age = int(input('Age : '))


class Employee(Person):
    def __init__(self):
        super()
        self.Id =0

    def getInput(self):
        super().getInput()
        self.Id=int(input('EmployeeID : '))
    
     

ObjPer = Employee()
ObjPer.getInput()

print(str(ObjPer.Name)+','+str(ObjPer.Id))
