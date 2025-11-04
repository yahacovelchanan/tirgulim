from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self,max_speed):
        self.max_speed=max_speed
    def permitted_speed(self):
        print(f"The permitted speed is {self.max_speed}")    
class Car(Vehicle):
     pass 
class Motorcycle(Vehicle):
    pass
       
             
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def manage(self):
        print(f"manager {self.name}")
class Developer(Employee):
    def write_code(self):
        print(f"write code {self.name}")
 

class Shape(ABC):
    @abstractmethod
    def area(self):
       pass
   
class Rectangle(Shape):
    def area(self):
        return super().area()   
        
class Circle(Shape):
    def area(self):
        return super().area() 
        
class Square(Shape):
    def area(self):
        return super().area()         
            
               
        