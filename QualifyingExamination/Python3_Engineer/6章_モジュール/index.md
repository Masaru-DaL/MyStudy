# 6章_モジュール
出題数 2問

## 1. モジュール 1/2
#### 1-1. モジュールとは
- プログラムの再利用性を高める事が出来る
  - 関数を再利用
  - クラスを再利用
  - プログラムに名前を付けて呼び出す

#### 1-2. Python標準の機能を呼び出す
書き方 -> `import モジュール名`
`import random`
`import math`

#### 1-3. 自作のモジュールを呼び出す
Python標準と同じ
`import fibo`

#### 1-4. 階層が異なるモジュールの呼び出し
- hogeディレクトリにあるfugaを呼び出す
書き方 -> `from hoge import fuga`

#### 1-5. 全モジュールを一気に呼び出す
- hogeディレクトリにある全部のモジュールは、`*`を使うと呼び出せる
`from hoge import *`

:::message alert
どのモジュールを呼び出したかが分かりにくくなるので非推奨
:::

#### 1-5. モジュールの検索パス
- モジュールをどこから探しているか、呼び出し先を表示
- 先頭から優先される

```python: sys
import sys
print(sys.path)
```
pathが表示される

#### 1-6. 自作のモジュールを呼び出してみる
- 3章_気楽な入門編で作成した`fibo.py`を呼び出してみます。(どこに格納しているかは格個人で違います)

1. 同じ階層に`fibo.py`があるとします。

```python: module
import fibo
print(fibo.main())
```
1
1
2
3
5
8
13
21
None

2. 違う階層にある場合
`my_module`ディレクトリにある`fibo.py`を呼び出します。

```python: my_module/fibo.py
from my_module import fibo
print(fibo.main())
```
結果は上と同じです。

#### 1-7. 「コンパイル済」 Pythonファイル
- `ファイル名.pyc` がコンパイル済み
  - `__pycache__`ディレクトリに保存される
  - 2回目以降の読み込み速度を速くする
  - 実行時間は変わらない
  - `.py`を変更するとコンパイルを自動的にやりなおす

:::message
日常的に意識する必要のないファイル
:::


## 2. モジュール 2/2
#### 2-1. モジュールが定義している名前を確認
- モジュールを調べる時にごくたまに利用される

1. `fibo.py`を確認する

```python: fibo
def main():
  a, b = 0, 1
  while b < 30:
    print(b)
    # a, b = b, a + b
    a_tmp = a
    a = b
    b = a_tmp + b

if __name__ == "__main__":
  main()
```

2. `fibo.py`の名前を確認する

```python: dir
import fibo
print(dir(fibo))
```
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'main']

#### 2-2. パッケージ
- 複数のモジュールを束ねたプログラム
- 他のモジュールと名前が被る心配が不要になる

```md:
keisan: トップレベルパッケージ
  - __init__.py: keisanパッケージの初期化
  - basic: サブパッケージ
    - plus.py
    - minus.py
  - advance: サブパッケージ
    - differential.py
    - integral.py
```

#### 2-3. (keisan)パッケージの呼び出し方法
- 以下のいずれでも良い

`import keisan.basic.plus`
`from keisan.basic import plus`
`from keisan import basic.plus`

#### 2-4. (keisan)パッケージの実行方法
:::message
実行する際には、import時の名前を書く
ファイル内で名前が被らなければ、以下のどの方法でも良い
:::

- import keisan.basic.plusの場合
`keisan.basic.plus.main()`

- from keisan.basic import plusの場合
`plus.main()`

- 2-6. from keisan import basic.plusの場合
`basic.plus`

#### 2-5. パッケージから`*`をimport
1. `__init__.py`が呼び出される
2. `__all__ = ["basic", "advance"]`のようにリストを定義し、サブパッケージを書く

このようにすると、`basic`と`advance`の両方が`*`で呼び出される。
※`*`を使わない場合は、空ファイルでも良い

#### 2-6. パッケージ内の相対パスによる呼び出し
- 自分から見て、深い階層か浅い階層か
  - 相対パスで呼び出す事ができる

:::message alert
相対パスは混乱を生みやすいので、絶対パスの方がおすすめのようです。
:::

