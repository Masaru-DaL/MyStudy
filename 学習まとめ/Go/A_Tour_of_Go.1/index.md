# A Tour of Go Basics
## 1-1. Packages
Goのプログラムは、**パッケージ(package)で構成される。

- package
使用する言語で利用できる「オブジェクト」や「関数」の宣言などを、関連するものごとにまとめたものを**パッケージ**と呼ぶ。

- Goの場合は？
  - Goでプログラムを作成する場合、必ず**main**パッケージが存在する必要がある
  - また、**main**パッケージ中に**main**関数が定義される必要がある

簡単に言うと、Goのコードはパッケージの宣言から始まる！

```go: package
# パッケージの宣言.
package main

# 使用したいパッケージをインポートする.
import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
}
```

- fmt
  - 文字列の入出力と、フォーマット(書式設定)に関する機能を提供するパッケージ
  - `print`関数などを使うためには`fmt`のインポートが必要

- math/rand
  - 乱数生成に関するパッケージ
  - `math/rand`は弱い乱数、`crypto/rand`は強い乱数
  - 強弱は乱数精度(暗号化などに適しているかなど)

## 1-2. Imports
インポート自体はPythonでもあったので違和感はない。
- 複数インポートする場合は括弧でまとめる。

```go: imports
import (
  "fmt"
  "math"
)
```

- 複数のインポートステートメントで書く事も出来る
```go: imports
import "fmt"
import "math"
```
**Goは先に示した括弧でまとめたスタイルの方が良い！**

## 1-3. Exported names
- 最初の文字が大文字で始まる名前
  - 外部パッケージから参照できる名前(exported name)
- 小文字で始まる名前
  - エクスポートされていない名前

- 手順
1. パッケージのインポート
2. パッケージがエクスポートしている名前を参照可能になる

`math`パッケージの円周率に関するモジュールを使用したい場合はexported nameを指定する！

```go: exported name
func main() {
	fmt.Println(math.Pi)
  # math.piはエラーになる
}
```
小文字から始まる方がいまいち理解出来てないが、一旦飛ばす。

## 1-4. Functions
関数は、0個以上の引数を取ることができる。

```go: Functions
package main

import "fmt"

# ad関数の引数(x, y)がintであることを宣言
# () の後のintは戻り値の型を定義している
func add(x int, y int) int {
	return x + y
}

# 引数に指定した数の計算結果をintで返す
func main() {
	fmt.Println(add(42, 13))
}
```
上記のように、変数名の**後ろ**に型名を書く必要がある。

**Goは、静的型付け言語である！！**
動的型付け言語しかやってこなかったので整理する。

- (架空説明的な言語で)C以外の言語の場合の型構文
```cd:
x: int
p: pointer to int
a: array[3] of int
```

- Goの場合
```go:
x int
p *int
a [3]int
```
違いは、簡潔にするためにコロンを削除していることやいくつかのキーワードを削除している。
**Goの型宣言は、左から右へと読む！**
(Cがらせん状に読み取られていることが指摘されている。)

## 1-5. Functions continued
2つ以上の引数が同じ型である場合には、最後の型を残して省略して記述できる

`func add(x int, y int)`
-> `func add(x, y int)`

## 1-6. Multiple results
```go:
func swap(x, y string) (string, string) {
	return y, x
}
```
戻り値の第一引数と第二引数を交換するには、戻り値を交換するだけで簡単にできる
`return y, x`

## 1-7. Named return values
戻り値となる変数に名前をつけることができる

```go: Named return values
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
```
`split(sum int)`で関数を定義
`(x, y int)`で`x`, `y`という名前を戻り値に付けている。

- 変数に名前を付けなかった場合
```go: not Named return values
func split(sum int) (int, int) {
	return sum * 4 / 9, sum - (sum * 4 / 9)
}
```

実際に書いてみて分かったが、変数名に`x`, `y`と付ける事で、`y`の戻り値の計算が楽に書けていたことがわかった。(`y = sum - x`)
変数名を付ける事で可読性も上がるため、実務には必須な技術と思われる。

## 1-8. Variables
`var ~`で変数を宣言することができる

`var c, python, java bool`
このように複数の変数名+最後に型を宣言する
結果、`c, python, java`の3つが全てbool型となる。
int型の場合は`var a, b int`とする。

## 1-9. Variables with initializers
initializers -> 初期化子
変数名に初期値を設定できるという解釈で良さそう。

`var i, j int = 1, 2` -> `var i, j = 1, 2`
このように初期値を数値で指定することで、型宣言(int)を省略する事ができる。

## 1-10. Short variable declarations
短い変数宣言
**関数**の中では、`var`宣言の代わりに、`:=`の代入文を使い、暗黙的な型宣言ができる

**なお、関数の外では型宣言が必要で、`:=`での暗黙的な宣言は利用できない！**

`k := 3`
`var k int = 3`(intは省略可能)
両方同じ型宣言をしている。

