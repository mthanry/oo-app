#name = "John Doe"
#greeting = f"Welcome, {name}!"
#name = "Kieran Wood"
#print(greeting) # Prints: Welcome John Doe!
#greeting = f"Welcome, {name}!" # Since it's recreated it picks up the new value of name
#print(greeting) # Prints: Welcome Kieran Wood!

import datetime

#appolo_11_launch = datetime.date(1959, 9, 13)
#falcon_9_first_launch = datetime.date(2010, 6, 4)
#print(falcon_9_first_launch > appolo_11_launch) # prints: True

#print(falcon_9_first_launch.year)

#current_datetime = datetime.date.today()
#print(current_datetime)




class Animal:
    counter = 0
    def __init__(self, species_name, regions, common_name):
        """A class to represent a generic animal

        Attributes
        ----------
            species_name : (str) 
            The technical species name of the animal regions : (list[str]) 
            A list of regions the animal is endemic to common_name : (str) 
            The colloquial name of the animal
        """
        self.species_name = species_name
        self.regions = regions
        self.common_name = common_name
        
        Animal.counter += 1

    def print_info(self):
        """Prints information about animal instance"""
        print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")



print(Animal.counter) # Prints 0; since no Animal's have been instantiated
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

#print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

arctic_fox = Animal("Vulpes lagopus",
    ["The Arctic"],
    "Arctic fox")

#print(Animal.counter) # Prints 2; since the Leopard Gecko, and Arctic fox have been instantiated

# Both below calls print 2; Class variables are also accessible in any instance
#print(arctic_fox.counter)
#print(leopard_gecko.counter)




class CookieBaker:
  def __init__(self, number_of_cookies):
    """ Example class that is used to show off the __init__ method.
    The __init__ method calls prints 'Cookie Baked' as many times as there are number_of_cookies.

    Attributes
    ----------
    number_of_cookies(int): How many cookies to bake
    """
    print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
    self.number_of_cookies = number_of_cookies
    for cookie in range(number_of_cookies):
      print("Cookie Baked!")


#CookieBaker(5)


from dataclasses import dataclass

@dataclass
class user:
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    name:str
    age:str
    sign_up_date:datetime.datetime
    birthday:datetime.datetime
    premium_member:bool

me = user("Michael Thanry", 43, datetime.date.today(), datetime.date(1977,5,12), True)

print(me.sign_up_date)