
class Panda:

    kind = "Anemls"

    def __init__(self, wight : str, age : int, place_of_living : str, feeding : str) -> None:
        
        self.wight = wight
        self.age = age
        self.place_of_living = place_of_living
        self.feeding = feeding

    def information1(self):
          return f"panda wight is:  {self.wight} ,it is age is:  {self.age} , lives in the: {self.place_of_living}, and he eats: {self.feeding}"

    def information2(self):
          return f"panda wight is:  {self.place_of_living} ," 
          

panda1 = Panda("360", 4 , "north_forest" , "meat")
panda2 = Panda("250", 3 , "south_forest" , "meat")
panda3 = Panda("460", 5 , "east_forest" , "meat")
panda4 = Panda("350", 4 , "west_forest" , "meat")

print(panda1.information1())
print(panda2.information2())

print(panda1.wight) 
print(panda2.age) 
print(panda3.place_of_living)
print(panda4.feeding)