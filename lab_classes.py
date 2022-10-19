# Using what you learned about classes , create a class to represent a Panda. The class should have the following:
class Panda:
    def __init__(self, gender: str, height: str, weight: int, age: int):
        # 4 Attributes
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age

    # 2 Methods
    def pandaWalking(self):
        print(
            f"The {self.gender} panda with {self.age} age, Starts to walk in the jungle.")

    def pandaSleeping(self) -> str:
        print(
            f"The {self.gender} panda with {self.age} age, Stop walk and starts to sleep.")


# Create 4 instances of the class Panda
panda1 = Panda('Female', '70 CM', '60 KG', '4 Years')
panda2 = Panda('Male', '84 CM', '59 KG', '3.5 Years')
panda3 = Panda('Female', '74 CM', '65 KG', '6 Years')
panda4 = Panda('Male', '77 CM', '62 KG', '2 Years')

# Print 1 attribute value
print("The gender of first panda is: ", panda1.gender)

# Call the two methods on each instance
panda1.pandaWalking()
panda1.pandaSleeping()
panda2.pandaWalking()
panda2.pandaSleeping()
panda3.pandaWalking()
panda3.pandaSleeping()
panda4.pandaWalking()
panda4.pandaSleeping()
