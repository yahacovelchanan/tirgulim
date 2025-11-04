from math import pi
from abc import ABC,abstractmethod
class Book:
    
    def __init__(self,title:str,author:str,content:str):
        self.title=title
        self.author=author
        self.content=content
    def __str__(self):
        pass   
class Saved_to_list:
    def __init__(self):
        self.books_list=[]
    def saved_to_list(self,book:Book):
        self.books_list.append(book)
    def print_list(self):
        for book in self.books_list:
            print(book)
            
        
        



class student:
    def __init__(self,name:str,grades:list[int]):
        self.name=name
        self.grades=grades
        
class calc_grades:
    def __init__(self):
        pass
    @staticmethod 
    def calculate_average(self):
        return sum(self.grades) / len(self.grades) 
                       
                       
class Order:
    def __init__(self,items:list[str],total_price:float):
        self.items=items
        self.total_price=total_price
      
class InvoicePrinter(Order):
    def __init__(self):
        pass
    def print_invoice(self):
        print(f"This is your shopping list {self.items}.And this is its price {self.total_price}")  
                               
class Shape(ABC):
     @abstractmethod
     def area():
        pass
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2 * pi
    
class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a**2
    
class Rectangle(Shape):
    def __init__(self,n,o):
        self.n=n
        self.o=o
    def area(self):
        return self.n * self.o    

             
                    
           
        
        
    
        
   
        

                                       
                                       
                                     