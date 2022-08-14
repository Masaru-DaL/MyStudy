# エラーと例外
出題数 4問

## 1. 例外と例外処理
#### 1-1. SyntaxError: invalid syntax
- 構文エラー
  - プログラムの文法が間違ってると表示される
  - エラー箇所の修正が必要

`for i in range(10)`
```c: error
    for i in range(10)
                      ^
SyntaxError: expected ':'
```
range(10)の直後にコロンが必要

#### 1-2. リスト内包表記の間違い
`[for i in range(10)]`
```c: error
    [for i in range(10)]
     ^^^
SyntaxError: invalid syntax
```
forの前に「式」が必要(例えばi, i+1など)

#### 1-3. 例外: exception-1
- 実行中に検知されたエラー
`print(10 / 0)`

```c:error
    print(10 / 0)
ZeroDivisionError: division by zero
```
0で割り算は出来ない為

#### 1-3. 例外: exception-2
- 未定義の変数を呼ぼうとした時のエラー
`sushi + "wasabi"`

```c: error
    sushi+"wasabi"
NameError: name 'sushi' is not defined
```
sushiが定義されていませんよ、と出る

#### 1-3. 例外: exception-2

