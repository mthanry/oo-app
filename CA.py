# Question 11
# 
num = int(input("Enter a number:"))

if num%2 == 0:
    print("the numberis even")
else:
    print(num,"the number is odd.")





# Question 10
# 
num_1 = int(input("Enter a number:"))
num_2 = int(input("Enter a second number:"))

for i in range(num_1, num_2+1): # adding one to include num_2 in the loop
    if i%2 == 0:
        print(i)



# Question 2
#
shopping_list = []

item_1 = input("Enter an item to add to your shopping:")
item_2 = input("Enter an item to add to your shopping:")
item_3 = input("Enter an item to add to your shopping:")
item_4 = input("Enter an item to add to your shopping:")
item_5 = input("Enter an item to add to your shopping:")

shopping_list.append(item_1)
shopping_list.append(item_2)
shopping_list.append(item_3)
shopping_list.append(item_4)
shopping_list.append(item_5)
print(shopping_list)
