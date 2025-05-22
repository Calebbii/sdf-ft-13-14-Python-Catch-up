# Python Catch up

# OOP(Object Oriented Programming)
# Organizes code using classes and objects

# Classes - A blueprint for creating objects
#         - data + functions

# Objects - An instance of a class
#         - a bundle of attributes(variables) and methods(functions)

# Decorators - Methods that take in another method/function
#            - Functions that modify the behavior of other functions/methods.
#            - @classmethod


# ORM(Object Relational Mapping)
# Maps python objects to the db tables
# Maps Python classes to database tables, and objects to rows

# SQLalchemy - CRUD basics


from car import Car
# Creating the Car Objects
car_one = Car("Audi", "Audi A4", 2023, "Black")
car_two = Car("Mazda", "CX-5", 2019, "Red")
car_three = Car("Volkwagen", "Golf", 2021, "Blue")


# Calling the class methods
car_one.drive()
car_two.stop()

# Changing the year
Car.change_year(car_one,-3)
Car.change_year(car_two, 5)

# print out 
print(f"{car_one.model}'s updated year is:  {car_one.year}")
print(f"{car_two.model}'s updated year is:  {car_two.year}")