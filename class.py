class Panda:
    #class attribute
    kind = "Animal"
    def __init__(self,habitat:str,weight:str,Lifespan:int,size:str):
        self.habitat = habitat
        self.weight = weight
        self.Lifespan = Lifespan
        self.size = size 

    def PandasHabitat(self) -> str:
        return f"The Panda natural habitat is the {self.habitat}."
    def PandaWeight(self)-> str:
        return f"and they mostly weight {self.weight} kg,it's {self.Lifespan} years old,and it hight around {self.size}."

Panda1=Panda("bamboo forests and mountain ranges", "70kg", 14, "1.0 m")
print(Panda1.PandasHabitat())
print(Panda1.PandaWeight())
print('-'*10)
Panda2=Panda("bamboo forests and mountain ranges", "90kg", 16, "1.2m")
print(Panda2.PandasHabitat())
print(Panda2.PandaWeight())
print('-'*10)
Panda3=Panda("bamboo forests and mountain ranges", "120kg", 25, "1.5m")
print('-'*10)
print(Panda3.PandasHabitat())
print(Panda3.PandaWeight())
print('-'*10)
Panda4=Panda("bamboo forests and mountain ranges", "135kg", 30, "1.9m")
print(Panda4.PandasHabitat())
print(Panda4.PandaWeight())
print('-'*10)

print(Panda.kind)