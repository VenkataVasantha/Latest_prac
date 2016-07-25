import animals

def main():

    dog = animals.Dog()
    cat = animals.Cat()

    print show_info(dog)
    print show_info(cat)

def show_info(creature):
    if isinstance(creature, animals.Mammals):
       creature.show_species()
       creature.make_sound()

    else:
        print 'Wrong Mammals'

main()