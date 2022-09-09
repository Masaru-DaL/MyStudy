class PersonJapanese:
    # クラス内に変数を作成する
    language = "Japanese"

    def __init__(self, name, age):
        self.name = name
        self.age = age


male1 = PersonJapanese("Takeshi", 18)
male2 = PersonJapanese("Satoru", 15)

print(male1.language)
print(male2.language)
