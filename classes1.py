
#definig a class 

class Panda:
    def __init__(self,name: str, origin: str, color: str, behaviour: str) -> None:
        self.name = name
        self.origin = origin
        self.color = color
        self.behaviour = behaviour

    def namecolor(self) -> str:
        return f"The name is {self.name}, and color of it is {self.color}"  

    def originBehaviour(self)-> str:
        return f"The origin is {self.origin}, and behaviour is {self.behaviour}"    


panda1 = Panda("panda1","black", "japan","quite")
panda2 = Panda( "Panda2","white","china","fast")
panda3 = Panda( "Panda3","black","japan","active")
panda4 = Panda( "panda4","white","china","friendly")

print(f"the first panda color is {panda1.color}")

#method 1
panda1.nameColor()
panda1.originBehaviour()

#method 2
panda2.nameColor()
panda2.originBehaviour()

#method 3
panda3.nameColor()
panda3.originBehaviour()

#method 4
panda4.nameColor()
panda4.originBehaviour()
