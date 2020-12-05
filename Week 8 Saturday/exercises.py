# class Line:
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
        

#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2

#         return ((x2-x1)**2 + (y2-y1)**2)**0.5

#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2

#         return (y2-y1)/(x2-x1)

# coordinate1 = (3,2)
# coordinate2 = (8,10)

# li = Line(coordinate1,coordinate2)

# print(li.distance()) # 9.433981132056603

# print(li.slope()) # 1.6


# class Cylinder:
#     PI = 3.14

#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius     

#     def volume(self):
#         print((self.height)*self.PI*(self.radius)**2)

#     def surface_area(self):
#         print(2*(self.PI * (self.radius)**2) + (2*self.PI*self.radius*self.height))


# # EXAMPLE OUTPUT
# c = Cylinder(2,3)
# c.volume() # 56.52
# c.surface_area() # 94.2

# class Account:

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit accepted!")

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             print("Funds Unavailable!")
#             self.balance -= amount
#         else:
#             print("Withdrawal accepted!")
#         return self.balance

#     def __str__(self):
#         return f"Account owner:{self.owner}, Account Balance:{self.balance}"

# my_account = Account("Michael", 1234.56)

# print(my_account)


# a= [0,1,2,3]
# b=a 
# print(b)
# a.pop()
# print(b)


def vol(rad):
    print(3.14 * rad*rad*rad * 4 * 3)
# Check
vol(2)