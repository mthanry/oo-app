"""
    =========== Challenge 1 =============

    Take an input from the command line, then
    convert it to an int and if it is even 
    print 'the number is even' otherwise print
    'the number is odd'.
"""
my_number = int(input("Pick a number:"))
if my_number / 2 == my_number //2:
    print(str(my_number) + " is even.")
else:
    print(str(my_number) + " is odd.")

"""
    =========== Challenge 2 =============

    Take an input from the command line, and 
    convert it to an int. Validate the number
    is within the range 1-5, and then for each
    possible value (1-5), write the code to make
    the input 11.

    I.e. Someone inputs 1 the result is 11, if someone
    inputs 2 the result is 11 etc. If someone puts in a
    number not in range (1-5) print:
        'value not between 1-5 please try again'
    
    Hint: You should have between 6-7 if/elif/else statements
"""
my_number = int(input("Pick a number:"))

if my_number<1 or my_number>5:
    print("Value not between 1-5 please try again.")
#else print(11)
elif my_number == 1:
    print (my_number+10)
elif my_number == 2:
    print (my_number+9)
elif my_number == 3:
    print (my_number+8)
elif my_number == 4:
    print (my_number+7)
elif my_number == 5:
    print (my_number+6)

"""
    =========== Challenge 3 =============

    There are functions in python that can be used
    to determine if strings contain certain characters.
    
    For example the function isdigit() returns True if
    ALL the characters in the string are digits. Here
    is an example of it's usage:
        
        numbers = "1234567"
        letters = "Hello 4"
        
        print(numbers.isdigit()) # prints True
        print(letters.isdigit()) # prints False
     
     There are two other similar functions called endswith()
     and islower(). 
     
     endswith() takes a string as an argument
     and returns true if the string it's being used on ends with
     the string provided.
     
     islower() returns true if the string provided is all lowercase
     
     Now take input at the command line, and using if statements print
     the following statements if conditions are met:
        1. if the string is all numbers print "All numbers"
        2. If the string is all lowercase print "All lowercase"
        3. If the string ends with "yes" print "Ends in yes"
        Otherwise print "None of the conditions have been met"
"""
