
class Panda:

     def __init__(self , name:str , native:str , color:str , weighs:str) -> None:
        self.color = color
        self.name = name
        self.native = native
        self.weighs = weighs

     def info1(self)->str:
        return f"name of panda is: {self.name}, and native in: {self.native}"
    
     def info2(self)->str:
        return f"color of panda is {self.color}, and weighs: {self.weighs}"


panda1 = Panda("Red Panda" , "eastern Himalayas and southweastern China" ,"Red" ,"between 3.2 and 15kg")

print(panda1.name)

print(panda1.info1())
print(panda1.info2())