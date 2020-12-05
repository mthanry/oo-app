# try:
#     f = open('testfile','w')
#     f.write('Test write this')
# except IOError:
#     # This will only check for an IOError exception and then execute this print statement
#     print("Error: Could not find file or read data")
# else:
#     print("Content written successfully")
#     f.close()

# def askint():
#     while True:
#         try:
#             val = int(input("Please enter an integer: "))
#         except:
#             print("Looks like you did not enter an integer!")
#             continue
#         else:
#             print('Good boy')
#             print(val)
#             break
#         finally:
#             print("Finally, I executed!")

# askint()

# #PB 1
# for i in ['a','b','c']:
#     try:
#         print(i**2)
#     except:
#         continue

# #PB 2
# x = 5
# y = 0

# try:
#     z = x/y
# except:
#     print('42 the answer to life the universe and everything, including dividing by 0')
# finally:
#     print('All done')

# # PB 3
# def ask():
#     while True:
#         try:
#             val = int(input('Enter an integer:'))
#         except:
#             print('Try again.')
#         else:
#             print(val ** 2)
#             break
# ask()

import cap
import unittest
