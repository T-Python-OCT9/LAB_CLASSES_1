# LAB_CLASSES_1


## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
'''- 4 Attributes
- 2 Methods
'''

### Create 4 instances of the class Panda , print 1 attribute value,  and call the two methods on each instance. 

class Panda:
    def __init__(self , color, hight, wight, type) -> None:
        self.color = color
        self.hight = hight
        self.wight = wight
        self.type = type

    def panda_look(self):
        print(f"Panda color is: {self.color}, his hight is: {self.hight} and he wight {self.wight}")
    
    def panda_type(self):
        print(f"The type of this panda is: {self.type}")

panda1 = Panda("brown", "2.70cm", "500kg", "giant panda")
panda1.panda_look()
panda1.panda_type()