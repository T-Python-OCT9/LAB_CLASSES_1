class Panda:

    Kind = "Animal"
    Color = "white"
    eye = "blue"
    weight = "100kg"

    def __init__(self, name : str, country : str, age : int) -> None:
        #initilizing the class
        #instance attributes / properties
        self.name = name
        self.country = country
        self.age = age

    def  type(self):
        if self.country== "china" : 
            return (f"this type of panda which live in {self.country} called Giant ")
        else:
           return ("I dont know")

    def How_long_live(self):
        age = 20 - self.age
        return age


test_1 = Panda("luli","china",10)
test_2 = Panda("noni","asia",20)
test_3 = Panda("lala","us",3)
test_4 = Panda("dana","usa",5)

print(Panda.Kind)

print(test_1.type()) 
print(test_1.How_long_live()) 
   