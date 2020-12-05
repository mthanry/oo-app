"""
    =========== Exercise 1 =============

    I have provided some starter code below
    that creates a result variable, and a number_1
    variable. Your goal is to make number_1 equal 11
    after the operations that have been done to it.
"""

result = 0
number_1 = 5
number_1 += 52

# Do more operations on number 1 until it equals eleven
number_1 //= 5

result = number_1
print(result == 11)


"""
    =========== Exercise 2 =============

    Take input from the command line, and convert it to
    an int. Now pick a range (i.e. 0-10), and create a set
    of conditional statements that prints the string
    representation of the number input by the user.

    For example if someone put in 8, then it would print 'eight'.
    
    Hint: Use if, elif and else statements.
"""

pick_one = int(input("Pick a number:"))

if pick_one == 0:
    print("Zero")
elif pick_one == 1:
    print("One")
elif pick_one == 2: 
    print("Two")
elif pick_one == 3:
    print("Three")
elif pick_one == 4:
    print("Four")
elif pick_one == 5:
    print("Five")
else:
    print("It's outside the [0-5] range.")

"""
    =========== Exercise 3 =============

    Before running the code below try to
    figure out which print statement will
    execute and why. Then uncomment the code
    and check if you were right.
"""

number = 0
number += 15
number //= 2
number *= 6
number -= 4

# should make 38

if number < 10:
     print("Less than 10")

elif 10 <= number <= 20:
     print("Between 10 and 20")

elif 20 <= number <= 30:
    print("Between 20 and 30")

elif 30 <= number <= 40:
     print("Between 30 and 40")

else:
     print("¯\_(ツ)_/¯")