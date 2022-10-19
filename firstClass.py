class panda :
    kind = "Animal"
    Type = "bear"
    classification = "predator"

    def __init__(self , name : str , contury : str , YearOfbirth : int , age : int ) -> None:
       self.name = name 
       self.contury = contury
       self.YearOfbirth = YearOfbirth 
       self.age = age


    def welcoming (self):
        print ("Hello the topic today is about pandas and we will take some exambles ..")

    def generalInfo(self) -> str:
        return f" our Examble panda for today is {self.name} , she was porn in {self.contury} , on {self.YearOfbirth} and her age is : {self.age}"

Panda1 = panda("Bao Bao", "Washington", "2013","9")
Panda2= panda("Mei" , "Washington","1998","24")
Panda3= panda("Gao Gao" , "San diego Zoo", "2011","10")
Panda4= panda ("Er shun","Toronto Zoo" , "2007","15")

Panda1.generalInfo()
Panda2.generalInfo()
Panda3.generalInfo()
Panda4.generalInfo()

    
#print(Panda1.welcoming())
#print(Panda2.generalInfo())

print (Panda4.age)

print ("The classification of the Panda is :", panda.classification)
 

