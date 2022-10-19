

'''

## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
- 4 Attributes
- 2 Methods


### Create 4 instances of the class Panda , print 1 attribute value,  and call the two methods on each instance. 

'''

class Panda:
    kind = "Animal"

    def __init__(self, name : str, city : str, color : str, size : str  ) -> None:
      
        self.name = name
        self.city = city
        self.color= color
        self.size= size

        
    def PandaFun1(self) -> str:
        return f"Panda name is: {self.name} ,He lives in: {self.city}"
    

    def PandaFun2(self) -> str:
        return f"Panda color is {self.color} ,The size of this panda is {self.size}"

panda1 = Panda("giant panda", "Sichuan", "red", "120kg")
print(panda1.name)

print(panda1.PandaFun1())
print(panda1.PandaFun2())

print(Panda.kind)

