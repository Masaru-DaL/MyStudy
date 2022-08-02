#　今回の開発のゴール
:::message
Flask-AppBuilderを使用してToDoアプリケーションの作成
:::

環境構築は済んでいるものとする。
済んでいない方は以下を参考にしてください。

1. [Flask + MySQL (Docker) の環境構築](https://zenn.dev/articles/556d3f3864cf51/edit)
2. [Flask-AppBuilder (Docker)でブラウザにアクセスする](https://zenn.dev/articles/b12f8b92492ada/edit)


AppBuilder自体の参考記事がほとんどないので、[公式ドキュメント](https://flask-appbuilder.readthedocs.io/en/latest/index.html#)を元に進めていきます。


# Viewの作り方
[参考ページ](https://flask-appbuilder.readthedocs.io/en/latest/views.html)

## 1. URLのみのルーティングでViewを表示する
```python: view.py
from flask_appbuilder import AppBuilder, expose, BaseView
from app import appbuilder

class MyView(BaseView):
    route_base = "/myview" # ①

    @expose('/method1/<string:param1>') # ②
    def method1(self, param1):
        # do something with param1
        # and return it
        return param1

    @expose('/method2/<string:param1>') # ③
    def method2(self, param1):
        # do something with param1
        # and render it
        param1 = 'Hello %s' % (param1)
        return param1

appbuilder.add_view_no_menu(MyView()) # ④
```

どういった記述がしてあるのか確認していきます。
(詳細までは分かりかねますが、こういった感じのことかな？という理解をします。)

:::message
公式ドキュメント自体にも書いてありますが、URLルーティングメソッドを`@expose`で装飾し、`@has_access`デコレータを追加して、これがセキュリティで保護されたメソッドであることをflaskに伝えています。
(1.では@has_accessを使用していません。)
:::

#### 1-1. route_base = "/myview"
ルーティングを定義しています。
`http://localhost:5000/`以下に`/myview`を打ち込みアクセス形にしています。

#### 1-2. @expose('/method1/<string:param1>')
ルーティングの`/myview`の後に`/method1/[任意の文字列]`を打ち込むと、打ち込んだ任意の文字列がviewとして表示されます。

#### 1-3. @expose('/method2/<string:param1>')
2とほぼ同じですが、`/method2/[任意の文字列]`を打ち込むと、hello+任意の文字列がviewとして表示されます。

#### 1-4. appbuilder.add_view_no_menu(MyView())
appbuilderの構文(だと思います)で、メニューを作成せず表示させます。

#### 1-5. アクセスしてみる
http://localhost:5000/myview/method1/john
http://localhost:5000/myview/method2/john

※johnは任意の文字列です
:::message
`view.py`などを変更した際には、一度`flask run`を終了し、再度`flask run --host 0.0.0.0 --port 5000`で起動し、変更を反映させてください。
:::

## 2. メニューの作成を伴うViewの表示(+@has_access)
パターン2として、先ほどの`view.py`を変更します。
メニューを作成し、アクセスするとViewが表示されるようにします。

```python: view.py
from flask_appbuilder import AppBuilder, BaseView, expose, has_access
from app import appbuilder


class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/') # ②
    @has_access
    def method1(self):
        # do something with param1
        # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param1>') # ④
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1

appbuilder.add_view(MyView, "Method1", category='My View')　# ①
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View') # ③
```

#### 2-1.　appbuilder.add_view(MyView, "Method1", category='My View')
`add_view`を使用すると、メニューに関連づけられたviewを追加出来ます。
メニュー名 -> `MyView`
MyView内にMethod1という名前で追加します。

#### 2-2. @expose('/method1/')
MyViewからMethod1を選択すると`http://localhost:5000/myview/method1/`にアクセスし、helloという文字列のviewが表示されます。
`@has_access`でセキュリティで保護されたメソッドですよーとFlaskに伝えています。

#### 2-3. appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
`add_link`は①で作成されたMyViewという名前のメニューにリンクを追加出来ます。
リンク名 -> Method2
リンクURL -> /myview/method2/john
MyView内のMethod2を選択すると`http://localhost:5000/myview/method2/john`にアクセスします。

#### 2-4. @expose('/method2/<string:param1>')
引数に指定されたparam1は③で入力されるリンク名`/myview/method2/john`の`john`に当たります。
なので、③のリンク先にアクセスすると、param1がreturnとなっているので、Goodbye + johnが表示されます。


## 3. look and feelを伴うviewの作成
公式の説明文を引用します
> Notice that these methods will render simple pages not integrated with F.A.B’s look and feel. It’s easy to render your method’s response integrated with the app’s look and feel, for this you have to create your own template. Under your project’s directory and app folder create a folder named ‘templates’. Inside it create a file name ‘method3.html’

:::message
ちょっと小難しい感じがするので、簡単に解釈すると、1と2のやり方だと見た目や感じが伴ってないからtemplatesフォルダにhtmlファイルなどを置いて、それを読み込むことでlook and feelを伴ったviewを作成しましょうという感じです
:::

#### 3-1. templates, htmlの作成
`create-app`でappを作成すると自動でtemplatesディレクトリが作成されているとは思いますが、ない場合は作成したappディレクトリの直下にtemplatesディレクトリを作成し、`method3.html`という名前でhtmlファイルを作成します。

```html: <PROJECT_NAME>/app/templates/method3.html
{% extends "appbuilder/base.html" %}
{% block content %}
    <h1>{{param1}}</h1>
{% endblock %}
```

公式から解釈すると、「appbuilder/base.html」を拡張し、ブロックコンテンツをオーバーライドしています。
(appbuilderが元々用意しているものを使って、それをオーバーライドしているという認識で良いはずです)

#### 3-2. MyViewクラスにメソッドを追加する
2.で作成した`view.py`の中のMyViewクラスにメソッドを追加します。
新しいテンプレートのレンダリングはappを作成した段階であるはずですが、なければ追加してください。
(記述する場所はmethod2の下でかまいません。)

```python: view.py
from flask import render_template

@expose('/method3/<string:param1>')
@has_access
def method3(self, param1):
    # do something with param1
    # and render template with param
    param1 = 'Goodbye %s' % (param1)
    self.update_redirect()
    return self.render_template('method3.html',
                           param1 = param1)

appbuilder.add_link("Method3", href='/myview/method3/john', category='My View')
```

3-1.で作成したテンプレートをレンダリングします。
メニューにmethod3が追加され、選択すると`http://localhost:5000/myview/method3/john`にアクセスし、Goodbye johnという文字列のviewが表示されます。

`self.update_redirect()`は、説明を見た感じだけだと理解しきれませんが、セッションやクッキーを利用する際(フォームなど)に便利な感じです。

`self.render_template`はバージョン1.3.0以降、すべてのビューテンプレートをレンダリングする必要があるようです。


## 4. フォーム ビュー
`view.py`と同じ階層に`form.py`を作成します。
`view.py`を記述し、作成した`form.py`をimportして呼び出します。

:::message alert
公式の通りにやると作成したform.pyのimportの記述が抜けているので注意です。
:::

#### 4-1. form.py
```python: form.py
from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm


class MyForm(DynamicForm):
    field1 = StringField(('Field1'),
        description=('Your field number one!'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    field2 = StringField(('Field2'),
        description=('Your field number two!'), widget=BS3TextFieldWidget())
```

```python: view.py
from flask import flash
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _

from . import appbuilder, db
from .form import MyForm


class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message = 'My form submitted'

    def form_get(self, form):
        form.field1.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash(self.message, 'info')

appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                     category="My Forms", category_icon="fa-cogs")
```
