'''
# LAB_CLASSES_1

## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
- 4 Attributes
- 2 Methods

### Create 4 instances of the class Panda , print 1 attribute value,  and call the two methods on each instance. 

'''


class Panda:
    
    def __init__(self,name: str, kind: str, color: str, behaviour: str) -> None:
        self.name = name
        self.kind = kind
        self.color = color
        self.behaviour = behaviour

    def nameColor(self) -> str:
        return f"The name is {self.name}, and color of it is {self.color}"  

    def kindBehaviour(self)-> str:
        return f"The kind is {self.kind}, and behaviour is {self.behaviour}"    


panda1 = Panda("panda1", "regular", "white and black", "very friendly")
panda2 = Panda( "Panda2","red panda","red","friendly")
panda3 = Panda( "Panda3","red panda","red","friendly")
panda4 = Panda( "panda4","red panda","red","friendly")

print(f"the first panda color is {panda1.color}")

#calling the method 1
panda1.nameColor()
panda1.kindBehaviour()

#calling the method 2
panda2.nameColor()
panda2.kindBehaviour()

#calling the method 3
panda3.nameColor()
panda3.kindBehaviour()

#calling the method 4
panda4.nameColor()
panda4.kindBehaviour()








    

    