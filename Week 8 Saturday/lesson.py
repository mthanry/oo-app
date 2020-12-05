## Inheritance

# class Animal:
#     def __init__(self):
#         print("Animal created")
#     def whoAmI(self):
#         print("Animal")
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#     def whoAmI(self):
#         print("Dog")
#     def bark(self):
#         print("Woof!")

# d = Dog()
# d.whoAmI()
# d.eat()
# d.bark()


## Polymorphism

# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name+' says Woof!'

# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name+' says Meow!' 

# niko = Dog('Niko')
# felix = Cat('Felix')

# print(niko.speak())
# print(felix.speak())

# or to iterate

#  


# Abstract class

# class Animal:
#     def __init__(self, name):    # Constructor of the class
#         self.name = name
#     def speak(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")

# class Dog(Animal):  
#     def speak(self):
#         return self.name+' says Woof!'

# class Cat(Animal):
#     def speak(self):
#         return self.name+' says Meow!'

# fido = Dog('Fido')
# isis = Cat('Isis')

# print(fido.speak())
# print(isis.speak())


# Special methods

# class Book:
#     def __init__(self, title, author, pages):
#         print("A book is created")
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self):
#         return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print("A book is destroyed")
#     def __eq__(self, other):
#         return self.title == other.title

# book = Book("Python Rocks!", "Jose Portilla", 159)
# other_book = Book("Python Rocks!", "Michael", 20)

# print(book)
# print(len(book))

# print (book == other_book)
# del book



# MAP function
##############
# def square(num):
#     return num**2

# my_nums = [1,2,3,4,5]

# # To get the results, either iterate through map() 
# # or just cast to a list
# for item in map(square,my_nums):
#     print(item)

# list(map(square,my_nums))

# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'even'
#     else:
#         return mystring[0]

# mynames = ['John','Cindy','Sarah','Kelly','Mike']

# print(list(map(splicer,mynames)))






# FILTER function
#################

# def check_even(num):
#     return num % 2 == 0 

# nums = [0,1,2,3,4,5,6,7,8,9,10]

# print(nums)
# print(list(filter(check_even,nums)))

# for n in filter(check_even,nums):
#     print(n)





# LAMBA function
#################
# def square(num):
#     result = num**2
#     return result

# print(square(2))

# # would become
# square = lambda num: num ** 2
# print(square(2))

# my_nums = [1,2,3,4,5]
# nums = [0,1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda num: num ** 2, my_nums)))
# print(list(filter(lambda n: n % 2 == 0,nums)))



# name = 'This is a global name'

# def greet():
#     # Enclosing function
#     #name = 'Sammy'
#     def hello():
#         print('Hello '+name)
#     hello()

# greet()




# x = 50

# def func():
#     global x
#     print('This function is now using the global x!')
#     print('Because of global x is: ', x)
#     x = 2
#     print('Ran func(), changed global x to', x)

# print('Before calling func(), x is: ', x)
# func()
# print('Value of x (outside of func()) is: ', x)







# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
#     else:
#         print("I don't like fruit")
# myfunc(fruit='pineapple')
# myfunc()

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass

myfunc('eggs','spam',fruit='cherries',juice='orange')