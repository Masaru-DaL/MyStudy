# JavaScriptnoの問題
JavaScriptの不備が原因となる脆弱性について

# DOM Based XSS
## 概要
JavaScriptによる処理の不備が原因でXSSとなる場合があり、DOM Based XSSと呼ばれている。
近年JavaScriptによる処理が相対的に増えてきており、DOM Based XSSがあるアプリケーションも増えてきている。

## 脆弱性が生まれる原因
- DOM操作の際に外部から指定されたHTMLタグなどが有効になってしまう機能を用いている
- 外部から指定されたJavaScriptが動くevalなどの機能を用いている
- XMLHttpRequestのURLが未検証である
- location.hrefやsrc属性、href属性のURLが未検証である

HTMLタグなどが有効になってしまう機能(関数やプロパティ)の例
- document.write() / document.writeln()
- innerHTML / outerHTML
- jQueryのhtml()
- jQueryのjQuery()、$()

evalインジェクションの原理でJavaScriptが動く機能
- eval()
- setTimeout() / setInterval()
- Functionコンストラクタ
外部からコントロール可能な値を上記に設定することにより、意図しないJavaScriptが実行されることになる。

URLにjavascriptスキームやvbscriptスキームが指定できるとJavaScriptが実行される機能
- JavaScriptのlocation.href
- a要素のhref属性やiframe要素のsrc属性など

## 対策
DOM Based XSSの原因は、外部から指定したHTMLタグ文字列がHTMLの要素に変換されてしまうことや、eval関数などに外部からの値を渡すことが原因なので、以下のいずれかにより文字がそのまま表示されるようにすることで対策になる。
### 適切なDOM操作あるいは記号のエスケープ
innerHTMLやdocument.writeの使用を避け、DOM操作によりテキスト要素を追加するか、textContentプロパティを使用することでDOM Based XSSを防ぐことができる。
例: innerHTMLプロパティをtextContentプロパティに置き換えることにより、DOM Based XSSは対策される。
document.writeについてはDOM操作では代替できないので、document.writeの使用をやめるか、HTMLエスケープによる対策となる。
### eval、setTimeout、Functionコンストラクタなどの引数に文字列形式で外部からの値を渡さない
evalやFunctionコンストラクタは本質的に危険なので避けるべきだが、どうしても使わなければならない場合は、外部からの値を英数字に限定する方法などで対策する。
### URLのスキームをhttpかhttpsに限定する
location.hrefやsrc属性やhref属性など、URLをとる属性値はスキーマがhttpかhttpsであることを確認する必要がある。
### jQueryのセレクタは動的生成しない
$()の引数を動的生成すると、セレクタの意味を変更させられる可能性があり、危険である。
$()の引数は原則として動的生成しないことが推奨される。
例えばfindメソッドを用いることで、動的にHTML要素を生成されることはなくなる。
しかし、findメソッドを用いた場合でもセレクタの構造を替えることはできてしまうので、値の検証も必要である。
既に$()の引数を動的に生成しているアプリケーションがあり緊急に修正しなければならない場合は、引数を検証するか、整数に変換する方法もある。
### 最新のライブラリを用いる
新しいjQueryは対策されており、使うだけでセレクタによるDOM Based XSSは防げるが、予防としてアプリケーション側でも引数は動的生成しないことが推奨される。
### XMLHttpRequestのURLを検証する
XMLHttpRequestのURLを外部から自由に指定できると、仮にXSSにならなくてもオープンリダイレクトと似た問題となり、画面の内容を改変されるなどの問題が生じる。
このため、XMLHttpRequestのURLは外部から指定できないようにすることが確実な対策だが、どうしてもURLを可変にしたい場合は、固定のテーブルを用いる方法が確実である。

# Webストレージの不適切な使用
