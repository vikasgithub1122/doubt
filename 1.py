# # custom __format__() method
# class Car:
#     def __format__(self, format):
#         if(format == 'colour'):
#             return 'Red'
#         return 'None'

# print(format(Car(), "colour"))


# class Human:
#     def __init__(self,name,age,gender,):
#         self.name=name
#         self.age=age
#         self.gender=gender
# c=Human('raju',26,'male')
# print(c.name)
# print(c.gender)
# print(c.age)


# class Human:
#     #class attribute
#     species = "Homo Sapiens"
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
        
# x = Human("Ron", 15, "Male") 
# y = Human("Miley", 22, "Female")
# print(x.name)
# print(y.name)
# print(f'Hi! my name is {x.name} and i am a {x.gender} and i am {x.age}')
# class car:
#     def __init__(self, name):
#         self.name=name
#         def moves(self):
#             print(f"{self.name} moves on the access")
# c=car("honda")
# print(c.name)


class Human:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def speak(self):
        return f"Hello everyone! i am {self.name}"
    
    def eat(self, favouriteDish):
        return f"I love to eat {favouriteDish}!!!"
    
    def car(self, car_name):
        return f"i love {car_name}"

x=Human("Ciri", 18, "female")
print(x.speak())
print(x.eat("momos"))
print(x.car("black scorpio"))        



class Human:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def discription(self):
        print(f"Hey! My name is {self.name}, i'm a {self.gender} and I'm {self.age}years old")
class Boy(Human):
    def schoolName(self,schoolName):
        print("i study in {schoolName}")
h=Human('lily', 32, 'girl')
h.discription()
h.schoolName('ABC Academy')
    
