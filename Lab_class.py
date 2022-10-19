class panda :

    
    def __init__(self,name_panda,panda_city_birth,panda_color,panda_age) -> None:
        self.name_panda = name_panda
        self.panda_city_birth = panda_city_birth
        self.panda_color = panda_color
        self.panda_age = panda_age
        
    def introduceSelf(self) -> str:
       return f"panda name: {self.name_panda}"

    def PandaSelfBirth  (self) -> str :
        return f"panda city:{self.panda_city_birth}"

Panda_1 = panda("kogma","china","black and white","10")
panda_2 = panda("ying","korea","black and red","25")
panda_3 = panda("yataro","japan","black and blue","15")
panda_4 = panda("naruto","thailand","black and yellow","20")


print(Panda_1.introduceSelf())
print(panda_2.PandaSelfBirth())
print(panda_3.introduceSelf())
print(panda_4.PandaSelfBirth())
