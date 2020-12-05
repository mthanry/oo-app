# # MAP function
#################
# def fahrenheit(celsius):
#     return (9/5)*celsius + 32

# temps = [0, 22.5, 40, 100]
# F_temps = map(fahrenheit, temps)

# #Show
# print(list(F_temps))



### LAMBDA function
###################
# temps = [0, 22.5, 40, 100]
# print(list(map(lambda x: (9/5)*x + 32, temps)))


### MAP() WITH MULTIPLE ITERABLES
#################################
# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [9,10,11]

# print(list(map(lambda x,y:x+y,a,b)))

# # Now all three lists
# # map will stop at the end of smalles list
# print(list(map(lambda x,y,z:x+y+z,a,b,c)))



### REDUCE function
###################
# from functools import reduce
# lst =[47,11,42,13]
# print(reduce(lambda x,y: x+y,lst)) # sums all items

# from functools import reduce
# lst=[47,11,42,13]
# print(lst)
# #Find the maximum of a sequence (This already exists as max())
# max_find = lambda a,b: a if (a > b) else b
# #Find max
# print(reduce(max_find,lst))




### FILTER function
###################
# #First let's make a function
# def even_check(num):
#     if num%2 ==0:
#         return True

# lst =range(20)
# print(list(filter(even_check,lst)))
# print(list(filter(lambda x: x%2==0, lst)))




### ZIP function
###################
# x = [1,2,3]
# y = [4,5,6]

# # Zip the lists together
# print(list(zip(x,y)))

# y = [4,5,6,7,8]

# # Zip the lists together
# print(list(zip(x,y)))

# d1 = {'a':1,'b':2}
# d2 = {'c':4,'d':5}

# print(list(zip(d1,d2)))
# print(list(zip(d1,d2.values())))

# def switcharoo(d1,d2):
#     """ swap keys and values
#     """
#     dout = {}
#     for d1key,d2val in zip(d1,d2.values()):
#         dout[d1key] = d2val   
#     return dout

# print(switcharoo(d1,d2))




### ENUMERATE() function
########################
# lst = ['a','b','c']

# for number,item in enumerate(lst):
#     print(number)
#     print(item)

# months = ['March','April','May','June']
# print(list(enumerate(months,start=3)))




### ALL() and ANY() function
############################
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False