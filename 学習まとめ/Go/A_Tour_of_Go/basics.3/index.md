# A Tour of Go Basics.3
## 3-1. Pointers
Goではポインタを扱える。
ポインタ？
参考: [Goで学ぶポインタとアドレス](https://qiita.com/Sekky0905/items/447efa04a95e3fec217f)
記事が古いのが気になりますが、いいねが多いのでこちらで理解を深めます。

- ポインタを理解するには前提知識が必要
1. プログラムのコンパイルから実行までの流れ
Goはコンパイラでコンパイルが必要である。

2. 変数とメモリとアドレス
- アドレスとは
  - 変数に値を代入し、コンパイルした時には、「メモリ上のある場所」に変数の値が格納される。
  - この「メモリ上のある場所」が「アドレス」というもの
  - アドレス番地は16進数で表される。(例: `0x1040a0d0`)

```go:
package main

import "fmt"

type Person struct {
	Name string
	Age int
}

func main() {
	// ポインタ型の変数を宣言する
	// pがポインタ変数
	// *Personポインタ型
	var p *Person

	p = &Person{
		Name: "太郎",
		Age: 20,
	}
	fmt.Printf("変数pに格納されているアドレス :%p", p)
}
```
変数pに格納されているアドレス :0xc000118018

- `&`オペレータ
  - 変数のアドレス番地を引き出す
  - `i := 42` -> `p = $i` (&iでiのアドレス番地を引き出す)

3. ポインタとポインタ変数
上記のコードに以下を追加して出力する
`fmt.Printf("p :%+v\n", p)`
-> p :&{Name:太郎 Age:20}

- `%+v`
`%+v`
構造体を出力する際に、%vの内容にフィールド名も加わる
`%v`
デフォルトフォーマットで対象データの情報を埋め込む
`\n`
言わずもがな、改行

ようするに、`p`を出力することで`&{Name:太郎 Age:20}`が出力されることが重要。
**変数`p`がポインタ変数となり、実際に`p`にはアドレスが格納されている。**

まだ続いているが、こんがらがりそうなので一旦終了。

## 3-2. Structs
struct(構造体)
なんとなくやってる事は分かるけど、理解しきれない。
クラスのような、関数のような、何が違うのか。

`type Person`で定義して、人は名前や性別、年齢、身長など様々な要素(フィールド)がある。
structはフィールドの集まり。という説明はなんとなく理解できる。

```go: struct
package main

import "fmt"

type Person struct {
	Name string
	Sex string
	Age int
	Height int
	Weight int
}

func main() {
	fmt.Println(Person{"Musashi", "男", 27, 182, 74})
}
```
{Musashi 男 27 182 74}
引数の順番は、フィールドを定義した順番と同じ

## 3-3. Struct Fields
structのフィールドには、ドット`.`を用いてアクセスする。

```go: struct(.)
package main

import "fmt"

type Person struct {
	Name string
	Sex string
	Age int
	Height int
	Weight int
}

func main() {
	Musashi := Person{"Musashi", "男", 27, 182, 74}
	fmt.Println(Musashi.Name)
}
```
Musashi

## 3-4. Pointers to structs
structのフィールドは、structのポインタを通してアクセスすることもできる。

```go: Pointers to structs
package main

import "fmt"

type Person struct {
	Name string
	Sex string
	Age int
	Height int
	Weight int
}

func main() {
	Musashi := Person{"Musashi", "男", 27, 182, 74}
	p := &Musashi
	p.Age = 1e9
	fmt.Println(Musashi)
}
```
{Musashi 男 1000000000 182 74}

- 1e9
  - よく小数点を省略する時に使う記法と同じで、1の後に0を9個付けるという意味

文字列へのアクセスはまた別途理解が必要。

## 3-5. Struct Literals
1. 構造体を定義する
2. 構造体を使って様々に派生できる
ということが言えるのだと思われる。

調べた結果:
Goはオブジェクト指向言語の様なクラスを持たない。
なのでクラスの継承も存在しない。
構造体でそのような事ができる。ということ。

## 3-6. Arrays
`var a [10]int`
これは変数`a`がint型で10個の配列を宣言しているということ。

```go: Arrays
package main

import "fmt"

func main() {
	// 1
	var a [2]string

	// 2
	a[0] = "Hello"
	a[1] = "World"

	// 3
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	// 4
	primes := [6]int{2, 3, 5, 7, 11, 13}

	// 5
	fmt.Println(primes)
}
```
1. `var a [2]string`で文字列で2個の配列を宣言
2. `a`のindex0, 1に文字列を入れている。
3. `a[0], a[1]`だとそれぞれの要素を出力し、`a`だと配列として出力している
4. `primes`に、配列の宣言と配列への要素の格納を同時に行なっている。
5. `primes`で出力しているので配列で出力されている。

- 出力結果
Hello World
[Hello World]
[2 3 5 7 11 13]
