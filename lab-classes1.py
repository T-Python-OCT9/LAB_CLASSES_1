'''# LAB_CLASSES_1


## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
- 4 Attributes
- 2 Methods


### Create 4 instances of the class Panda , print 1 attribute value,  and call the two methods on each instance. 
'''





class Panda:
    kind="animale"
    type="mammals"
    found_in="china"


    # Initializer
    def __init__(self,name:str,height:str,weight:str,fur:str)->None:
        self.height=height
        self.weight=weight
        self.name=name
        self.fur=fur

    def print_info(self)->str:
        return f"The {self.name} can grow up to {self.height}and {self.weight}\n"
    def fur_func (self)->str:
        return f"The {self.name} have a {self.fur} coat\n"
        

panda1=Panda("giant panda","1.7m","91 kg","white & black")
panda2=Panda("red panda","0.6m","65 kg","red &black")
panda3=Panda("Qinling panda","1.4m","70 kg","white &brown")

print("tha pand live in",Panda.found_in)
print(panda1.print_info())
print(panda2.fur_func())