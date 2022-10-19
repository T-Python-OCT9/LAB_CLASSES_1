class Panda :
     kind = "Animal"
    
  

def __init__(self,name,city,color,age) -> None:
        self.name= name
        self.city = city
        self.color = color
        self.age = age

def introduceSelf(self) -> str:
       return f"panda name: {self.name}"

def PandaSelfCity  (self) -> str :
        return f"panda city:{self.city}"

Panda1 = Panda("kog","china","black and white","10")
panda2 = Panda("joog","korea","green ","15")
panda3 = Panda("yare","sura","black","12")
panda4 = Panda("nanoo","chin","white","24")

print(Panda1.introduceSelf())
print(Panda1.PandaSelfCity())

print(panda2.introduceSelf())
print(panda2.PandaSelfCity())

print(panda3.introduceSelf())
print(panda3.PandaSelfCity())

print(panda4.introduceSelf()) 
print(panda4.PandaSelfCity()) 