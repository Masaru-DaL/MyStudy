class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, name):
        self.name = name
        print(f"Hello, {self.name}")


male1 = Person("Takeshi", 18)
# female1 = Person("Hanako", 18)

male1.say_hello("Hanako")
