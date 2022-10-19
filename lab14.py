


class panda:

    sizee = 'More than 110 kilograms'
    Native_Habitat = 'Mountins And Forsets'
    Eating_Habits = 'Mouse'
    Sleap_Habits  = 'More than 12 Hours in the day'
    Colors = 'Black and White'


    def __init__(self, name ,size ,colors) ->None:

        self.name = name

        self.size = size

        self.colors = colors

    def inS_colors(self)-> str :

        return f'Panads Have tow colors {self.Colors} its togather'

    def inS_H_sleap(self)-> str:

        return f'Panda can sleap {self.Sleap_Habits}'

    


    
PandaMeles = panda('Cocnat','More than 140 KG','White and Black')

PandaFemels = panda('Panda', 'less than 115 KG ','White and Black')

PandaBabies = panda('Little Cocnat','less than 75 KG','White and Black')

PandaFemels = panda('Panda', 'less than 115 KG ','White and Black')

#There is no more 3 

print('Panda meles size',PandaMeles.size)

print(PandaFemels.inS_H_sleap())

print(PandaMeles.inS_colors())