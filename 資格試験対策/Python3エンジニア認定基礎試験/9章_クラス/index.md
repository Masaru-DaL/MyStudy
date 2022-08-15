# 9章_クラス
出題数 2問

## 1. クラス part.1
#### 1-1. クラス
- 実体を表現するための雛形のこと
- Personというクラス(雛形)を考えてみると
  - Name, Age, etc..で具体的なPersonが決まる
  - これによって出来たものを**インスタンス**と呼ぶ
  - インスタンスを作る際の雛形のことを**クラス**と呼ぶ

#### 1-2. オブジェクト
- クラスやインスタンスの総称
  - Pythonでは、あらゆるデータ(関数、クラス、数字など)がオブジェクトである
  - オブジェクトには型(type)がある
    - 数字ならint型
    - 文字ならstr型

#### 1-3. Personクラスからインスタンスを生成
`Person`クラスを定義し、そこからインスタンスを生成する。
1つのクラスから複数のインスタンスを作成する事が出来る。

```python: class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


male1 = Person("Takeshi", 18)
male2 = Person("Kaoru", 15)

print(male1.name)
print(male2.name, male2.age)
```
Takeshi
Kaoru 15

`self`は自分自身を指す。

#### 1-4. インスタンス変数へのアクセス
上記の`print`のように、
`インスタンス名.インスタンス変数名`でアクセス出来ます。
また、データを書き換えることも出来る。

上で作成したインスタンスを書き換えます。
male1は名前と年齢を変える。
male2は年齢だけを変える。

```python: class
male1 = Person("Takeshi", 18)
male2 = Person("Kaoru", 15)

male1.name, male1.age = "Yosaku", 30
male2.age = male2.age + 3

print(male1.name, male1.age)
print(male2.name, male2.age)
```
Yosaku 30
Kaoru 18
　
#### 1-5. メソッド
- クラス内で定義された関数
`def メソッド名(self):` と書く。
Personクラスに挨拶をするメソッドを追加する。
`say_hello`の引数に名前を入れるとその人に挨拶をする。

```python: method
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
```
Hello, Hanako

#### 1-6. クラス変数
- クラスの中で変数を定義すると、そこから作成される全てのインスタンスにクラス変数が共有される。
日本人クラスを定義し、言語を日本語という変数を作成します。
複数のインスタンスからクラス変数を呼び出すと同じものが呼び出されます。

```python: class
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
```
Japanese
Japanese


## 2. クラス part.2
#### 2-1. 継承
- クラスが持つ機能を別のクラスに受け渡す
  - クラス同士で同じ機能のメソッドを持たせること
  - 親クラスのメソッドを上書き(**オーバーライド**)することも出来る

#### 2-2. 具体的に
- 親クラス
  - `Person`
    - 食べる
    - 寝る

- 子クラス
  - `Man`, `Woman`
    - 継承するメソッド
      - 食べる
      - 寝る
    - 各クラス独自のメソッド
      - 性別(男性, 女性)

```python: inheritance
class Person:
    def eat(self, food):
        print(f"{food}を食べる")

    def sleep(self, time):
        print(f"{time}時に寝る")


class Man(Person):
    sex = "man"


class Man(Person):
    sex = "woman"
```
親クラスから継承を用いて新たにクラスを定義するには、
`class 新しいクラス名(親クラス名):` とします。

#### 2-3. 継承しているメソッドを確認する
```python: inheritance
# 親クラスのメソッドを確認
person = Person()
person.eat("おにぎり")
person.sleep(11)

# Manクラスの継承したメソッドの確認
man = Man()
man.eat("おにぎり")
man.sleep(11)
```
おにぎりを食べる
11時に寝る
おにぎりを食べる
11時に寝る

PersonもManも、eat, sleepのメソッドを持っていることが分かります。

#### 2-4. 親クラスは、子クラス独自のメソッドを持たない
```python: inheritance
# 子クラス独自のメソッド
print(man.sex)

woman = Woman()
print(woman.sex)
```
man
woman

```python: inheritance
# 子クラスだけのメソッドを親クラスで呼び出そうとすると
person.sex
```
    person.sex
AttributeError: 'Person' object has no attribute 'sex'
> Personオブジェクトにsexという属性がありません。
というエラーが出ます。


