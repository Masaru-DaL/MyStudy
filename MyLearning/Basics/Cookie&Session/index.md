# CookieとSessionの違いとは

## 1. CookieとSessionの概要

### 1-1. なぜCookieとSessionが存在するのか

**HTTP通信がステートレスなプロトコルで「状態」を持てないため**
状態とは何を指すのか。
一例だが、ログインした後の状態とする。
ログインした後、ページを閉じて、開くとまたログインしなくてはいけないというのは面倒すぎる。これを解決してくれるのがCookieとSessionである。

### 1-2. CookieとSessionの関係

この2つの関係を間違えてはいけない。
**Cookieを使って、Session状態を保持する**

## 2. Cookie

正式名称は「HTTP Cookie」だが、単にCookieとも表記されるので、Cookieと表記されていたらHTTP Cookieのことだと思って良い。

Cookieとは、HTTPにおけるブラウザとサーバの間で用いられる**ウェブブラウザに保存された情報のこと**を指す。ユーザ識別やセッション管理を実現する目的などに利用される。

参照: [HTTP Cookie](https://ja.wikipedia.org/wiki/HTTP_cookie)

## 3. Session

参照: [Session](https://ja.wikipedia.org/wiki/%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF))
