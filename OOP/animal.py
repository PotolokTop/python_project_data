class Animal:
    def __init__(self, name, weight):
        self.__name = name # private field
        self.weight = weight # public property

    def get_name(self): # getter
        return self.__name
    
    def set_name(self, name): # setter
        self.__name = name

animal = Animal("Daniel", 100) # set object

class Cat(Animal): # inhabitance
    def __init__(self):
        print("meow")
        # super().__init__(name, weight) # superclass = Animal


        