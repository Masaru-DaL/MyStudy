class Person:
    def eat(self, food):
        print(f"{food}を食べる")

    def sleep(self, time):
        print(f"{time}時に寝る")


class Man(Person):
    sex = "man"


class Woman(Person):
    sex = "woman"


# 親クラスのメソッドを確認
person = Person()
person.eat("おにぎり")
person.sleep(11)

# Manクラスの継承したメソッドの確認
man = Man()
man.eat("おにぎり")
man.sleep(11)

# 子クラス独自のメソッド
print(man.sex)

woman = Woman()
print(woman.sex)

# 子クラスだけのメソッドを親クラスで呼び出そうとすると
person.sex
