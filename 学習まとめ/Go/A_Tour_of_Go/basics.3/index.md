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

## 3-7. Slices
スライス(の概念)はpythonと同じ感じ

## 3-8. Slices are like references to arrays
```go: slice
package main

import "fmt"

func main() {
	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println(names)

	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)
}
```
[John Paul George Ringo]
[John Paul] [Paul George]
[John XXX] [XXX George]
[John XXX George Ringo]

スライスで取得した部分の要素の変更が可能。
`b := names[1:3]` -> `b[0] = "XXX"`

## 3-9. Slice literals
配列の流れとしては、
1. 配列の宣言
   1. 何個入る配列なのか
   2. 型を宣言
2. 配列に要素を格納

これを同時に行える時点で、何個入る配列なのかという部分は省略可能。

3-8のコードを、
`[4]string` -> `[]string`にしても良いということ。

実務においては何個入る配列かを明示的にしたほうがいいシーンもあるかもしれない。

## 3-10. Slice defaults
pythonと同様

## 3-11. Slice length and capacity
length -> 実際の要素の個数
capacity -> 基底配列の長さ, 最大収納量
```go: Slice length and capacity
package main

import "fmt"

func main() {
	// 1
	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	// 2
	// Slice the slice to give it zero length.
	s = s[:0]
	printSlice(s)

	// 3
	// Extend its length.
	s = s[:4]
	printSlice(s)

	// 4
	// Drop its first two values.
	s = s[2:]
	printSlice(s)
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
```
- 前提知識
配列の容量が不足した場合、新しい配列を大きなサイズでメモリ確保して元データ参照範囲をコピーする。

1. 配列の宣言と要素の格納(最初に6個格納しているのでこれがcapとなる)

2. 1の基底配列から取得しているので、実際の個数は0、capは6

3. ここが一番のキモ！
2の配列から取りたい、となった時に要素が何も入っていないため、1の配列から要素を取ってくるという流れになります。
なので、1の配列のindex0, 1, 2, 3を取ってくるため、len4, cap6となる。
参考: [Go言語「A Tour of Go」のsliceでわからないことがあります](https://teratail.com/questions/155045)

4. 3から取得します。
3の配列は[2 3 5 7]
len4、cap4です。
`[2:]`を指定すると5, 7が取得され、len2, cap4となります。

## 3-12. Nil slices
