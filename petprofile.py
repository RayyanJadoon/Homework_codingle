class Pet:
    def __init__(self):
        print("A pet was created.")


pet1 = Pet()


class PetProfile:

    school = "My Pet School"

    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal
        self.age = age

    def show_pet(self):
        print("Name:", self.name)
        print("Animal:", self.animal)
        print("Age:", self.age)
        print("School:", PetProfile.school)
        print()


pet2 = PetProfile("Buddy", "Dog", 3)
pet3 = PetProfile("Mittens", "Cat", 2)

pet2.show_pet()
pet3.show_pet()