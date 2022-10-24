
class Panda :
    type = "anmal"

    def __init__(self, name : str, wighe : str, tell  : str , loc : str) -> None:
        self.name = name
        self.wighe = wighe
        self.tell = tell
        self.loc = loc

    def eating(self):
       return     "panda is eating"

    def wigetoll(self)-> str:
        return     (f"The wighe is {self.wighe} ,and live in {self.loc}")

a1 = Panda('panda','','','')
a2 = Panda ('panda','150kg','','Japan')

print(a1.eating())
print(a2.wigetoll())
