class Car:
    # Attributes
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Methods
    def drive(self):
        print("The " + self.model + " of color " + self.color + " is being driven")

    def stop(self):
        print("This " + self.model + " has stopped")

    # Decorators - Methods that take in another method/function
    # cls - a reference to the class itself (not an instance)
    @classmethod
    def change_year(cls,car,year_delta):
        car.year += year_delta
        return car.year


# car_one = Car()
# car_two = Car()

# print(car_one)
# print(car_two)

# car_one.model = "Audi"

# print(car_one.model)