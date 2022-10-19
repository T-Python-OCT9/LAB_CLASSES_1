class Panda:
    #class attribute
    kind = "anamle"
    color = "white"
    size = "big"
    number = "123"

    def __init__(self, name : str, wight : str, national : str, locatin : str) -> None:
        self.name = name
        self.wight = wight
        self.national = national
        self.locatin = locatin

    def introduceSelf(self) -> str:
        return f"It is {self.name} , it is wight {self.wight} ,it is national {self.national},it is locatin {self.locatin} " 
    
    def greet(self):
        return f"Welcome ! , {self.name}"

anamle = Panda("coco", 300 , "chine" ,"home")
anamle2 = Panda("bobo", 400 , "japan" ,"street")
anamle3 = Panda("dodo", 350 , "ksa" ,"trach")
anamle4 = Panda("toto", 500 , "qtar" ,"home1")
print(anamle2.greet())
print(anamle2.introduceSelf())
print(anamle3.greet())
print(anamle3.introduceSelf())
print(anamle4.greet())
print(anamle4.introduceSelf())
print(anamle.greet())
print(anamle.introduceSelf())
print()
print(anamle.name, anamle.wight)
print()
print(Panda.color)

