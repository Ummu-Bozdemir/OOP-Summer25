class Animal:
    def _init_(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def show_info(self):
        return f"{self.name} ({self.group}) - Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}"


animals = [
    Animal("Cat", "Mammals", 4, ["jumping", "climbing"]),
    Animal("shark", "Mammals", 4, ["swimming", "barking"]),
    Animal("Eagle", "Birds", 2, ["flying", "hunting"]),
    Animal("Frog", "Amphibians", 4, ["jumping", "swimming"]),
    Animal("Snake", "Reptiles", 0, ["slithering", "hunting"])
]

for animal in animals:
    print(animal.show_info())
