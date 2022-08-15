class Person:
    def eat(self, food):
        print(f"{food}を食べる")

    def sleep(self, time):
        print(f"{time}時に寝る")


class Man(Person):
    sex = "man"

    def eat(self, food):
        print(f"{food}をたくさん食べた")


man = Man()
man.eat("ラーメン")
man.sleep(11)
