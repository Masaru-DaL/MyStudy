class Person:
    def eat(self, food):
        print(f"{food}を食べる")

    def sleep(self, time):
        print(f"{time}時に寝る")


class Man(Person):
    sex = "man"


class Man(Person):
    sex = "woman"


# 親クラスのメソッドを確認
person = Person()
person.eat("おにぎり")
person.sleep(11)

# Manクラスの継承したメソッドの確認
man = Man()
man.eat("おにぎり")
man.sleep(11)
