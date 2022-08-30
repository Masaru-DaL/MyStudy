# A Tour of Go Lesson.1
Goチュートリアルの最初のレッスン

## 1-1. Packages
Goのプログラムは、**パッケージ(package)で構成される。

- package
使用する言語で利用できる「オブジェクト」や「関数」の宣言などを、関連するものごとにまとめたものを**パケージ**と呼ぶ。

- Goの場合は？
  - Goでプログラムを作成する場合、必ず**main**パッケージが存在する必要がある
  - また、**main**パッケージ中に**main**関数が定義される必要がある

簡単に言うと、Goのコードはパッケージの宣言から始まる！

```go: package
package main

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
