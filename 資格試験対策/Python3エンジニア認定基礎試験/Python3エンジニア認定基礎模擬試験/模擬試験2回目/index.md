## Pythonの特徴
 Pythonは柔軟な配列や集合、ディクショナリといった、非常に高水準のデータ型を組み込みで持つ。データ型の一般性が高いためPythonの対応可能な問題領域はAwkより広いが、Perlと比べると同程度である。

**データ型の一般性が高いためPythonの対応可能な問題領域はAwkより広いが、Perlと比べると同程度である。**が間違い。

データ型の一般性が高いためPythonの対応可能な問題領域は**Awkよりもずっと広く**、**Perlと比べてさえ広く**、その上たいていのことは他の言語と同程度以上に簡単に出来る。


## 変数に対しての指定
- 問題
```md:
次の変数Zenに関して指定した場合、実行時にエラーとならないものはどれか。

Zen = 'BeautifulIsBetterThanUgly'
```

- 回答を間違った答え
  - `Zen[10] = 'a'`

一見出来そうではあるが、文字列は不変であるため、indexを指定して新しい値を入れることは出来ないため、エラーが起こる。
`TypeError: 'str' object does not support item assignment`

- 正答
  - `Zen[1000:10000]`

#### スライスの理解を深める
`>>> Zen = 'BeautifulIsBetterThanUgly'`

`>>> Zen[0:4]` # index[0] ~ index[3]
'Beau'

`>>> Zen[:4]` # 左を省略した場合 [0:4] という指定になる
'Beau'

`>>> Zen[4:]` # 右を省略した場合 [4:最後まで]という指定になる
'tifulIsBetterThanUgly'

`>>> Zen[4:-1]` # この場合は index[4] ~ index[-1]の1個手前までとなる
'tifulIsBetterThanUgl'

`>>> Zem[:]` # 左右を省略した場合は全てを指定している
'BeautifulIsBetterThanUgly'

##### オーバーした数を指定した場合
`>>> Zen[1000:]` # スタートの数がないので何も出力されない
''

`>>> Zen[:1000]` # 0~最後までという指定になる
'BeautifulIsBetterThanUgly'

`>>> Zen[1000:1000]` # スタートの数がオーバーしている
''

- 正答
  - `Zen[1000:10000]`

これは何も出力されないが、エラーとはならないという所を覚えておく必要がある。


## 
