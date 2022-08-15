class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


male1 = Person("Takeshi", 18)
male2 = Person("Kaoru", 15)

male1.name, male1.age = "Yosaku", 30
male2.age = male2.age + 3

print(male1.name, male1.age)
print(male2.name, male2.age)
