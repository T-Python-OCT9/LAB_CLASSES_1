


class Panda :
    type = "anmal"

    def __init__(self, name : str, wighe : str, tell  : str , loc : str) -> None:
        self.name = name
        self.wighe = wighe
        self.tell = tell
        self.loc = loc
    
    def eating(self):
       return     "f{panda} is eating"
        
    def wigetoll(self)-> str:
        return     (f"The panda is {self.wighe} ,and live in  {self.loc}")



a1 = Panda('panda','','','')

print(a1.eating())

a2 = Panda ('panda','222kg','','china')

print(a2.wigetoll())


