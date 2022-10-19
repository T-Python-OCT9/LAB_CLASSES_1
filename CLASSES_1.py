'''
# LAB_CLASSES_1


## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
- 4 Attributes
- 2 Methods


### Create 4 instances of the class Panda , print 1 attribute value,  and call the two methods on each instance. 


'''
#create a class to represent a Panda. The class should have the following:
# 4 Attributes
# 2 Methods
class animals :


    the_animal = "Panda"

    def __init__(self , idd : str , type1 :str  , age :int  , child : int  ):
        # 4 Attributes
        self.idd = idd
        self.type1 = type1
        self.child = child
        self.age = age 

    # 1 Methods
    def info (self) :
        return f"the id for panda {self.idd } ,  typr  {self.type1} the panda ahas been since {self.age} "


  # 2 Methods
    def the_parents (self) :
        if self.child !=0:
          return f"the paanda have child : {self.child} " 
        else:
          return  f" no child :"



p1 = animals("d12", "pandaa", 20 , 2 )
p2 = animals("d4", "pp", 4 , 0 )

print(p1.idd , p1.type1 , p1.age , p1.child)
print(p2.idd , p2.type1 , p2.age , p2.child)

print(p1.info())
print(p2.info())

print(p1.the_parents ())
print(p2.the_parents ())



   

