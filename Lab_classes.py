'''
LAB_CLASSES_1

'''

class Panda:
    # class attribute 
    kind = "Animal"
    
    #Initializing + 4 Attributes
    def __init__(self, name : str , age : str , speed : int ,  happiness_level : int ) -> None:
        self.name = name
        self.age = age
        self.speed = speed
        self.happiness_level = happiness_level

    #2 Methods:
    #1:
    def declare(self) -> str :
        return f"This Panda's name is : {self.name}  | age : {self.age}  | speed : {self.speed} "
    #2:
    def feed(self , happiness) -> int:
        self.happiness_level += happiness
        return f" Happiness level is : {self.happiness_level} "
        


#reate 4 instances (obj) of the class Panda  
Panda1 = Panda("Klwe" , "10" , 20 ,  70)
Panda2 = Panda ("GU GU" , "20" , 18 , 50)
Panda3 = Panda("Spot" , "5" , 14 , 90)
Panda4 = Panda("Rocky" , "15" , 22 ,  85)


# print 1 attribute value,
print(f"name : { Panda3.name} | age : {Panda3.age} | speed : {Panda3.speed} | happiness level : {Panda3.happiness_level}")

#  and call the two methods on each instance.
print(Panda1.declare())
print(Panda1.feed(10))

print(Panda2.declare())
print(Panda2.feed(10))

print(Panda3.declare())
print(Panda3.feed(10))

print(Panda4.declare())
print(Panda4.feed(10))
