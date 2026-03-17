#OOPs - Object Oriented Programming 
# 1. creating a class using class className:

class Student:
    x = 10
print(Student)

# 2. creating an object using object = classname(parameter)

class Student:
    x = 10
s1 = Student()
print(s1.x)


# 3. creating multiple objects
class Student:
    x = 10  

s1 = Student()
s2 = Student()
print(s1.x)
print(s2.x)
# output: 10
#         10


# 4. deleting object- using del keyword 
class Student:
    x = 10  
s1 = Student()
s2 = Student()
print(s1.x)
del s1
print(s1.x)
# output: 10
#         10
#         NameError: name 's1' is not defined


# 5. __init__ () method is a constructor. It calls automatically when an object is created.
# used to assign initial value to object properties
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("John", 21)
print(s1.name)
print(s1.age)
# output: John  
#         21


# 6. set default values in __init__ method
class Student:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
s1 = Student("Alice")
print(s1.name)
print(s1.age)
# output: Alice
#         0


# 7.  self is a reference to the current instance of the class 
# used to access properties and methods that belong to the class.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return (f"{self.name} is {self.age} years old.")
    
s1 = Student("Indu",21)
print(s1.greet())
#output: Indu is 21 years old.


# 8. calling methods with self

class Animal:
    def __init__(self, name):
        self.name = name

    def cat(self):
        return "Hello" + self.name
    
    def dog(self):
        msg = self.cat()
        print(msg + " from dog method")

a = Animal("Buddy")
a.dog()



# 9. accessing properties(variables)
# using . notation

class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand)   
print(car1.model)


# 10. modifying properties
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model  

car1 = Car("Toyota", "Corolla")
print(car1.brand )
print(car1.model)

car1.brand = "Honda"
print(car1.brand)
print(car1.model)   

# output: Toyota Corolla
#         Honda Corolla


# 11. Delete properties
# using del keyword

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand)   
print(car1.model)

del car1.model
print(car1.model)   # This will raise an AttributeError since model property is deleted
          
# output: Toyota
#         AttributeError: 'Car' object has no attribute 'model'



# 12. class Properties v/s object properties
# defined outside __init__ method are class properties(belong to class itself)
# defined inside __init__ method are object(instance) properties

class Person:
    species = "Human" #class property

    def __init__ (self, name):
        self.name = name  #object property

p1 = Person("Alice")
p2 = Person("Bob")

print(p1.species)  #Accessing class property using object
print(p2.species)       

print(Person.species)  #Accessing class property using class name
print(p1.name)       #Accessing object property
print(p2.name)
print(Person) #Accessing class itself

# output: Human
#         Human
#         Human
#         Alice
#         Bob
#         <class '__main__.Person'>



# 13. Methods with Parameters
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
    
calc = Calculator()
print(calc.add(10,12))
print(calc.multiply(10,2))
# output: 22
#         20




# 14. method accessing properties
# methods can access and modify object properties using self

# Accessing object properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return (f"{self.name} is {self.age} years old.")
    
p1 = Person("Indu", 21)
print(p1.get_info()) #accessing properties using method (get_info)
# output: Indu is 21 years old.



# Modifying object properties
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def celerate_birthday(self):
        self.age += 1

p1 = Person("Indu", 21)
print(p1.name)  # Output: Indu
print("Current age:",p1.age)  # Output: 21
p1.celerate_birthday()
print("Updated age:",p1.age)  # Output: 22



# 15. The __str__() Method
# The __str__() method is a special method that controls what is returned when the object is printed.
# used to return a string representation of an object 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
book1 = Book("1984", "George Orwell")
print(book1)  # This will invoke the __str__() method   
# output: '1984' by George Orwell


# 16.  Multiple Method 
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectangle(5, 10)
print("Area:", rect.area())            # Output: Area: 50   
print("Perimeter:", rect.perimeter())  # Output: Perimeter: 30
# output: Area: 50
#         Perimeter: 30 




# 17. Deleting Methods
# using del keyword

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectangle(5, 10)
print(rect.perimeter())      # Output: Perimeter: 30

del rect.perimeter  # Deleting the perimeter method

print(rect.area())            # Output: Area: 50   
print(rect.perimeter())      # This will raise an AttributeError since perimeter method is deleted
# output: 30
#         50
#         AttributeError: 'Rectangle' object has no attribute 'perimeter'




# 18. Creating Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
#Use the parent class to create object, and then execute the introduce() method:
person1 = Person("Chandu", 50)
print(person1.introduce())

# output: Hello, my name is Chandu and I am 50 years old.

#Creating a child class
class Student(Person):
    pass
# Use the Student class to create an object, and then execute the introduce method:

x = Student("Indu", 21)
print(x.introduce())
# output: Hello, my name is Indu and I am 21 years old. 



# 19. Adding the __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
print(p1.name)
print(p1.age)
# output: Alice
#         30

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)



#20. Senario based question
# Student class - id, name, phone number,; take exam, enroll in class
# BCA Student - additional info is - number of years of course, subjects; course type - graduation or post graduation
# MCA student - addidional info - number of years of course work, subjects, course type and methods in addition to student class - viva
class Student:
    def __init__(self, id, name, phn_no,exam, enroll, viva):
        self.id = id
        self.name = name
        self.phn_no = phn_no
        self.exam = exam
        self.enroll = enroll
        self.viva = viva

class BCAStudent(Student):
    def __init__(self, id, name, phn_no, exam, enroll, no_of_years, subjects, course_type):
        super().__init__(id, name, phn_no, exam, enroll, viva=None)
        self.no_of_years = no_of_years
        self.subjects = subjects
        self.course_type = course_type

class MCAStudent(Student):
    def __init__(self, id, name, phn_no, exam, enroll, no_of_years, subjects, course_type, viva):
        super().__init__(id, name, phn_no, exam, enroll, viva)
        self.no_of_years = no_of_years
        self.subjects = subjects
        self.course_type = course_type

student = Student(1, "Indu", "7411198251", "Midterm", "CS101", "Viva Pending")
bca_student = BCAStudent(1, "Indu", "7411198251", "Midterm", "CS101", 3, ["C", "DM", "CNN"], "Graduation")
mca_student = MCAStudent(2, "Kavya", "9876543210", "Final", "CS201", 2, ["AI", "ML", "DS"], "Post Graduation", "Viva Completed")

print(f"Student: {student.name}, Phone Number: {student.phn_no}, Exam: {student.exam}, Enroll: {student.enroll}, Viva: {student.viva}")
print(f"BCA Student: {bca_student.name},Number of year:{bca_student.no_of_years} Course Type: {bca_student.course_type}, Subjects: {bca_student.subjects}, Viva: {bca_student.viva}")
print(f"MCA Student: {mca_student.name},Number of year:{mca_student.no_of_years} Course Type: {mca_student.course_type}, Subjects: {mca_student.subjects}, Viva: {mca_student.viva}")
