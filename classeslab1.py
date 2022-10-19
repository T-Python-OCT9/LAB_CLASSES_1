# this is classes lab 1 - 19 oct - ghadah alharbi 


class Panda:
    type="animal"

 
    def __init__(self, name : str, size : str, age : int , weight: float ) -> None:
        self.name = name
        self.size = size
        self.age = age
        self.weight=weight 


    #this take a random number from 0 to 3 and prints a fact abot pandas 
    def panda_fact(self , number ):
        panda_list=['THEY SPEND A LOT OF THEIR DAY EATING','PANDAS CAN SWIM AND EVEN CLIMB TREES','BAMBOO IS CRITICAL TO THEIR DIET','A panda year is equivalent to three human years']
        return panda_list[number]


    # this method take the panda's name and the person who is responsible to take care of it (animal keeper)
    def panda_d(self, panda_name , panda_keeper):
        l1={panda_name: panda_keeper}
        print(  l1.get(panda_name), "responsible for: ", panda_name)


# creating 4 instance 
p1=Panda("panda1", "3 feet", 10 , 40)
p2=Panda("panda2", "4 feet", 20 , 80)
p3=Panda("panda3", "3 feet", 15, 60)
p4=Panda("panda4", "5 feet", 30 , 100)

# printing 1 attribute value
print(p1.name)

#calling the two methods on each instance
print(p1.panda_fact(0))
print(p2.panda_fact(1))
print(p3.panda_fact(2))
print(p4.panda_fact(3))

p1.panda_d(p1.name , "khalid")
p2.panda_d(p2.name , "ghadah")
p3.panda_d(p3.name , "rashid")
p4.panda_d(p4.name , "asmaa")







