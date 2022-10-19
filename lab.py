class Panda:
    
    kind = 'animal' # class attribute
    
    def __init__(self,gender,nationality,national_id,age): # initilizing the class
        # instance attributes
        self.gender = gender
        self.nationality = nationality
        self.nationality_id = national_id
        self.age = age

    def panda_data(self) -> str:
        return f"the panda gender is {self.gender}\nnationality:{self.nationality}\nnationality_id:{self.nationality_id}\nage:{self.age}"

    def panda_nationality(self) -> str:
        return f'the panda nationality is: {self.nationality}'

# objects 
first_panda = Panda('male','russia','20002121','11')
second_panda = Panda('female', 'usa','20002122','12')
third_panda = Panda('male', 'canda', '22222222', '13')
fourth_panda = Panda('male', 'saudi', '12121212', '12')

print(f'the first panda nationality is :{first_panda.nationality}')  # print 1 attribute value

# calling the two methods on each instance
print(first_panda.panda_data())
print(first_panda.panda_nationality())

print(second_panda.panda_data())
print(second_panda.panda_nationality())

print(third_panda.panda_data())
print(third_panda.panda_nationality())

print(fourth_panda.panda_data())
print(fourth_panda.panda_nationality())







    
    