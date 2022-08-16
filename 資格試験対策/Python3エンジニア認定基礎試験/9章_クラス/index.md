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

#### 2-5. メソッドの上書き(オーバーライド)
親クラスからeat, sleepのメソッドを継承していますが、eatメソッドを新たに定義、sleepは継承したままにしてみます。

```python: override
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
```
ラーメンをたくさん食べた
11時に寝る

eatメソッドは新たに定義したものが実行され、sleepは親クラスで定義されたものが実行されました。

#### 2-6. 多重継承
- 複数のクラスを継承すること

```python: multiple_inheritance
# 親クラスからChildクラスを作成
class Child(Person):
  ...

# Personから作成されたMan,Childを継承するBoyを作成
class Boy(Man, Child):
  ...
```
:::message
この場合、メソッド, データ　の探索順は
Boy -> Man -> Child -> Person の順番で探索されます
(Man -> Childは継承した時の引数順)
:::

## 3. クラス　part.3
#### 3-1. 例外はクラス
`Exception`クラスを継承して自分で例外クラスを作る事が出来る。
新たなクラスを作成する時の引数に指定する。

```python: Exception
class MyError(Exception):
    pass
```

#### 3-2. イテレータ(反復子)
- 「データの流れを表現する」オブジェクト
- 自身を戻り値とする`__iter__`メソッド、次の要素を返す`__next__`メソッドを持つ

:::message
リストやタプル、辞書、集合は典型的な**反復可能オブジェクト**である。これらは内部に**イテレータ**を持ち、for文などで要素を反復的に処理する際には、Python内部で自動的にそれが使われるようになっている。
なので、自分で実際に書くことは少ない。
:::

- 反復可能オブジェクトとは
  - 「要素を一度に1つずつ返せる」オブジェクト
  - それが内包するイテレータを返す`__iter__`メソッドを持つ

例えば。
```python: iterator
class Reverse:
    # 引数にdata(整数)を渡すと、文字数を計算する
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    # 文字数が0なら例外処理
    # 文字をindex-1(逆)から返す
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


reverse = Reverse("spam")
for char in reverse:
    print(char)
```
m
a
p
s

#### 3-3. ジェネレータ
- 繰り返し処理を書く時に頻繁に使う

- ジェネレータの特徴
  - return文ではなく、「yield 値」という「yield式」を書く

```python: generator
# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]

# for char in reverse("game"):
#     print(char)

def word(data):
    for s in data:
        yield s

for one_word in word("game"):
    print(one_word)
```
g
a
m
e

上のは参考で出てきている文字を逆から出力する関数です。
回数指定の式がわからなかったので、順番に出力する方を作りました。
引数に文字を指定すると一つずつ文字を返す関数を定義し、その関数を用いて一文字ずつ出力するものを使用しています。

:::message
Pythonのジェネレータとは、戻り値を「yield」で返すジェネレータ関数です。
上の関数で分かるように、受け取った文字列をfor文で1文字ずつ取り出し、yieldで返します。

**このジェネレータ関数を作った時点では要素数が決まっていません。**
**他から要素を与えられて初めて確定するのがジェネレータの特良であると言えます。**
:::

- 追記
`Reverse`関数のrangeの引数の書き方が分からなかったのですが、理解したので追記です。
参考: [［解決！Python］range関数を使いこなすには
](https://atmarkit.itmedia.co.jp/ait/articles/2011/20/news018.html)

> range(0, 10, 3) -> 0, 3, 6, 9

- range(0, 10, 3)
  - 0
    - start(初期値)
  - 10
    - stop(最終値)
  - 3
    - step(差分)
これを当てはめます。

```python: Reverse
def reverse(data):
    # game -> 4文字 - 1, (3, -1, -1)
    # index3からindex0まで-1ずつ取得
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

for char in reverse("game"):
    print(char)
```
:::message
引数に`game`を指定したとして、gameは4文字です。
`range(len(data)) -1, -1, -1`は`3, -1, -1`となります。
stopの-1は、最終値が0という意味です。
gameの時はindex3(e)から-1ずつ文字を取得し、indexに入れます。
`yield data[index]`となっているので、1文字ずつデータを返します。nextで次の要素を取り出せます。
:::

#### 3-4. next()
- next()で順に取り出せます。

```python: next
reverse_word = reverse("game")
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))
```
e
m
a
g

- next()で文字数が0になった後に実行すると`StopIteration`という例外を吐いて終了します。

```python: next
reverse_word = reverse("game")
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))
```
e
m
a
g
...
    print(next(reverse_word))
StopIteration

#### 3-5. ジェネレータ式
- リスト内包表記でコンパクトに記述が可能

```python: generator
# sum(i*i for i in range(10))を出力

print(sum(i*i for i in range(10)))
```
285

(range10 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
[0*0, 1*1, ... 9*9]
を`sum`で足している。
