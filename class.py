class Panda:
    def __init__(self, type:str, length:str, weight:str,age:str) -> None:
        self.type=type
        self.length=length
        self.weight=weight
        self.age=age

    def typePanda(self):
        return f"the type is {self.type}"

    def printInfo(self):
        return f"the length of panda is {self.length}, his weight is {self.weight} and his age is {self.age}"

    

    
    

       

#instances of the class Panda 

panda1=Panda("Red panda","30cm","10kg","4 years")
panda2=Panda("Giant panda","10cm","90kg","4 years")
panda3=Panda("Red panda","40cm","15kg","4 years")
panda4=Panda("Giant panda","15cm","120kg","4 years")

#print one ttribute value

print("to print one ttribute value:\nthe age for this panda is:",panda1.age)

#print method 
print("-"*20)
print("the information for panad1 is :\n",panda1.printInfo(),"\nand the method for panda type is :\n",panda1.typePanda())
print("-"*20)
print("the information for panad2 is :\n",panda2.printInfo(),"\nand the method for panda type is :\n",panda2.typePanda())
print("-"*20)
print("the information for panad3 is :\n",panda3.printInfo(),"\nand the method for panda type is :\n",panda3.typePanda())
print("-"*20)
print("the information for panad4 is :\n",panda4.printInfo(),"\nand the method for panda type is :\n",panda4.typePanda())