
class Panda:

    # class attribute
    kind = "animal"

    def __init__(self, name: str, weight: str, height: str, foundin: str, fur: str) -> None:
        # initilizing the class
        # instance attributes / properties
        self.name = name
        self.weight = weight
        self.height = height
        self.foundin = foundin
        self.fur = fur

    def introducePanda(self) -> str:
        return f"common name: {self.name} ,they eat a lot and their body weight: {self.weight}pounds also height: {self.height} and they found in:{self.foundin}"

    def FactAboutPanda(self) -> str:
        return f"{self.name} has Fur color it {self.fur}. "


panda1 = Panda("Giant panda", "91", "1.5", "china", "white and black")

panda2 = Panda("red panda", "56", "0.6", "chine,Napal,Bhutan", "red and black")
panda3 = Panda("oinling panda", "70", "1.2", "chine", "white and brown")
panda4 = Panda("oinling panda", "70", "1.2", "chine")
print(panda1.name, panda1.foundin)
print(panda1.introducePanda())
print(panda2.introducePanda())
print(panda1.FactAboutPanda())
print(panda2.FactAboutPanda())
# accessing the class atrributes
print(Panda.kind)
