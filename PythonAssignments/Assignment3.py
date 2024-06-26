# 1. Create a dog object that will inherit all the variables and methods of the parent class Animal
# and display it.

class Animal:
    def __init__(self, name:str, sound: str, legs:int, tail:bool):
        self.name = name
        self.sound = sound
        self.legs = legs
        self.tail = tail

    def print_animal(self):
        has_tail = 'has tail' if self.tail else 'not having tail'
        print(f' {self.name} has {self.legs} legs and {has_tail}. It sounds {self.sound}')

dog = Animal('Dog', 'Bow Bow', 4, True)
dog.print_animal()

cat = Animal('Cat', 'Meyao', 4, True)
cat.print_animal()

hen = Animal('Hen', 'Clock', 2, False)
hen.print_animal()

#################################################################################################
# 2.Demonstrate the working of Polymorphism by creating two classes -Car and Bike.
# Display the information like name, color, and number of wheels.
class vehicle:
    def __init__(self,model:str, color:str, wheels:int):
        self.model = model
        self.color = color
        self.wheels = wheels

    def display_details(self):
        # print(f'This car\'s model is {self.model} in {self.color} color and {self.wheels} wheels.')
        print(f'This is vehicle class')

class car(vehicle):
    def __init__(self, model: str, color: str, wheels: int):
        super().__init__(model, color, wheels)
    def display_details(self):
        print(f'This car\'s model is {self.model} in {self.color} color and {self.wheels} wheels.')

class bike(vehicle):
    def __init__(self,model:str, color:str,wheels:int):
        super().__init__(model, color, wheels)
    #     self.model = model
    #     self.color = color
    #     self.wheels = wheels

    def display_details(self):
        print(f'This bike\'s model is {self.model} in color is {self.color} and {self.wheels} wheels.')

car_obj = car('Ford', 'Green', 4)
car_obj.display_details()

bike_obj = bike('Honda', 'Black',2)
bike_obj.display_details()

#################################################################################################
# 3.Create a list of tuples containing the 5 planets of our solar system along with their moons as-earth having 1 moon, Jupiter having 79 moons,
# Saturnhaving 82 moons, Uranushaving 27 moons and Neptunehaving 14 moons.
# Sort the list according to the ascending number of moons along with the names of planet using Lambda function.
# Display both original and sorted list.

planets = (('earth',1),('Jupiter', 79),('Saturnhaving', 82),( 'Uranus', 27), ('Neptunehaving', 14))
sorted_tuple = sorted(planets,key = lambda a: (a[1],a[0]))
print('Original: ',planets)
print('Sorted: ',sorted_tuple)

#################################################################################################
# 4.Create two functions -fillup and use, which uses a global variable as tank.
# Use the global variable in both the functions to return the quantity of fuel present in the tank after filling up
# the tank and after using the fuel of the tank. Show the working of two functions only. It is not necessary to
# display the outputs.
class gas:
    global tank
    def fillup(self, gas_usage):
        self.tank = gas_usage
        return self.tank

    def use(self,gas_usage):
        self.tank = gas_usage
        return self.tank

g = gas()
print(f'the quantity of fuel present in the tank after filling up the tank {g.fillup(200)} ')
print(f'after using the fuel of the tank {g.use(100)}')

##################################################################################################
# 5.Write a program to depict the use of multiple inheritance. The program should contain 4 classes
# -class 4 should inherit from class 2 and class 3. Similarly, class 2 should inherit from class 1.
# Class 3 should inherit from class 1. Each class should have its own print statement.

class class1:
    def __init__(self):
        print('This is class1')

class class2(class1):
    def __init__(self):
        print('This is class2')
        super().__init__()

class class3(class1):
    def __init__(self):
        print('This is class3')
        super().__init__()

class class4(class2, class3):
    def __init__(self):
        print('This is class4')
        super().__init__()

c = class4()

##################################################################################################
# 6.Use Getter and Setter method to set the name and age of a person. Moreover, get the name and age
# of the same person
class person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def setter_person(self,name,age):
        self.name = name
        self.age = age
    def getter_person(self):
        print(f'Person\'s name is {self.name} and age is {self.age}')

p = person()
p.getter_person()
p.setter_person('Person1',10)
p.getter_person()