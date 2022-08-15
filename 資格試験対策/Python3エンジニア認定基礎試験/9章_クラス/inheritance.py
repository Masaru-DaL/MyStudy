class Person:
    def eat(self, food):
        print(f"{food}を食べる")

    def sleep(self, time):
        print(f"{time}時に寝る")


class Man(Person):
    sex = "man"


class Man(Person):
    sex = "woman"
