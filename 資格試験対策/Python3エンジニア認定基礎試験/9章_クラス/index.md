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
