# A Tour of Go Lesson.1
Goチュートリアルの最初のレッスン

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
