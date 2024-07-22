class Animal:
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age
    def __str__(self):
        return f'''INFO:   Name = {self.name}, 
        Species = {self.species},
        Age = {self.age}'''
    def Habitat(self):
        return'Forest is the Major Habitat of Animals except for Humans.'
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name, "Dog", age)
    def Habitat(self):
        return f'{Animal.Habitat(self)} Urban areas are also a habitat for Dogs Specifically'

print(A := Animal('Kratu', 'Human', 18))
print(A.Habitat())
print(D := Dog('George',5))
print(D.Habitat())