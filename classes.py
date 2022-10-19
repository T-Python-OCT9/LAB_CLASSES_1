class Panda:
    #class attribute
    kind = "Animal"
    Id_Animal = "12345678"
    ageA = 4
    coloerA = "white"

    def __init__(self,name,age,id,coloer)->None:
        #initilizing the class
        #instance attributes / properties
        self.name = name
        self.age = age
        self.id = id
        self.coloer = coloer

    def PrintAnimal(self):
        print(f"Animal name is:{self.name} \nAge of animal: {self.age}\nID of animal is: {self.id}\nColoer of Animal is: {self.coloer}")

    def ColoerIsWhite(self)->bool:
        if self.coloer == "White":
            return True
        elif self.coloer != "White":
            return False
        else:
            return False
    

Panda1 = Panda("Bobii",4,"111111","White")
Panda2 = Panda("Bannty",3,"222222","Black")

print(f"Welcom to Panda {Panda.kind} Program...")
print("Name the first Panda is: ",Panda1.name)

print("All data of Panda.....\n")
Panda1.PrintAnimal()
Panda2.PrintAnimal()

print("\n\nIs the Panda White?.....\n")
print(f"{Panda1.name} is: ", Panda1.ColoerIsWhite())
print(f"{Panda2.name} is: ", Panda2.ColoerIsWhite())



