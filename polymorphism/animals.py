class Mammals:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print 'I am a ', self.__species

    def make_sound(self):
        print 'Grrr!!!!'

class Dog(Mammals):
    def __init__(self):
        Mammals.__init__(self, 'Dog')

    def make_sound(self):
        return 'Bow!!!!'

class Cat(Mammals):
    def __init__(self):
        Mammals.__init__(self, 'Cat')

    def make_sound(self):
        print 'Meow!!!!!'