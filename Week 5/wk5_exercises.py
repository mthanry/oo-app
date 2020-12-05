
import datetime # SEE: https://docs.python.org/3/library/datetime.html and the extras module for details

"""
    =========== Exercise 1 =============
    Write the estimate_planks function so that it returns the correct
    number of planks (use integer division to avoid complication).

    Example:


"""
class Contractor:
    def __init__(self, plank_length = 1):
        """A Demo class representing a construction Contractor.
        
        Attributes
        ----------
        plank_length(int): The length of wooden planks in feet; Default: 1
        
        Methods
        -------
        estimate_planks: Estimates the amount of planks needed to build a structure based on provided length.
        """
        self.plank_length = plank_length
    
    def estimate_planks(self, length):
        """Estimates the amount of planks needed to build the structure, based on the length

        Parameters
        ----------
        length(int): How long the structure that needs to be built is.
        """
        number_of_planks = length // self.plank_length
        return f"You need {number_of_planks} plank(s) of wood to build this wall"

dave = Contractor(2)
print(dave.estimate_planks(10)) # Should be 5 planks

billy = Contractor(5)
print(billy.estimate_planks(225)) # Should be 45 planks




"""
    =========== Exercise 2 =============
    Write a user class that has 3 attributes and 1 method:
        Attributes:
            1. name(str): users full name
            2. birthday(datetime.date): Users birthday as a datetime object
            3. premium (boolean): True or false based on if user is a premium user or not
        Method:
            1. next_birthday: A method that returns a string of the users birthday this year, if it is today then return 'Happy Birthday!' instead.
    
"""
class User:
    def __init__(self, name, birthday, premium):
        self.name = name
        self.birthday = birthday
        self.premium = premium

    def next_birthday(self):
        TODAY = datetime.date.today()
        if (self.birthday.month == TODAY.month) :
            return(f"Happy Birthday")
        else:
            return f"{self.birthday.month} {self.birthday.day} {TODAY.year}"


#john = User("John Doe", datetime.date(1995,10,25), True)

#print(john.next_birthday()) # You will have to validate this yourself
#print("John Doe" in john.name)  # Should print True
#print(john.premium) # Should Print True

"""
    =========== Exercise 3 =============
    Take the previous user class from before, and add a class docstring to it.
    For more details on docstrings and their formatting check out: https://github.com/canadian-coding/posts/tree/master/2019/July/25th%20-%20Docstrings%20in%20python
"""
