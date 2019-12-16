---
marp: true
title: Computing
description: Let's computing! Made to lecture in ttc.
url: https://www.ttc-net.co.jp/
---

# 本日は

オブジェクト指向プログラミングをします。

---

## 問題(イントロダクションより再掲)

AさんとBさんは同僚で、同じ道沿いに住んでいます。
毎日その道を通って、駅から会社に一緒に向かいます。
AさんはBさんよりも駅に近く、駅から1km。Bさんは1.5kmの位置に住んでいます。
ある日、いつもBさんが来る時間にAさんが家の前で待っていると、寝坊をしたBさんから連絡がありました。
「寝坊した！今から家を出る！走って追いつくから、先に行ってて！」
BさんがAさんに追いつくには、いつもよりどれだけ早く走らないといけないでしょうか？

---

## AさんとBさんをプログラム化する

---

AさんとBさんは家から駅まで一本道を進む

-----Bさん-----Aさん----------駅----------

---

[p5.js](https://p5js.org/get-started/)

* Processingの亜種
* HTML5のcanvasに図形を描ける
* グラフィック関連のサポートもある

---

## コーディング

---

プロジェクトのルートディレクトリを作成

```shell
mkdir work
cd work
mkdir myproject
cd myproject
```

---

index.htmlを作成

```shell
touch index.html
code index.html
```

---

### エディタ

[Visual Studio Code](https://code.visualstudio.com/download)

[キーボードショートカット](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
* Ctrl+P と Ctrl+Shift+` と Ctrl+J (Windows) がほとんど

---

[index.html](https://p5js.org/get-started/)
```html
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/npm/p5@0.10.2/lib/p5.js"></script>
    <script src="./sketch.js"></script>
  </head>
  <body>
  </body>
</html>
```

---

sketch.jsを作成

```
touch sketch.js
code sketch.js
```

---

### JavaScriptについて超簡単に

[JavaScript とは何か?](https://developer.mozilla.org/ja/docs/Web/JavaScript/About_JavaScript)

> JavaScript® (よく JS と略されます) は第一級関数を持つ軽量、インタプリタ方式、オブジェクト指向の言語です。Web ページ向けのスクリプティング言語としてもっとも知られていますが、ブラウザ以外の多くの環境でも使用されています。JavaScript はプロトタイプベースの動的なスクリプティング言語であり、オブジェクト指向、命令型、関数型のプログラミング方式をサポートします。

---

#### 一級関数

```
var function sum(a, b) {
  return a + b;
}
var sumObj = {
  name: 'Sum',
  operation: sum
}
console.log(sumObj.sum(1, 2))
// => 3
```

---

#### Webページ向け

```
window.location.href = '/about.html';
```

windowがいる！(windowは省略可能。(`location.href = ...`))

```
window.document.getElementById('nav-access');
// => <ul id="nav-access">...</ul>
```

documentがいる！(windowが最初に作られる。)

[DOMとwindowが作られるのは大体こんなイメージ](https://gigazine.net/news/20180323-rendering-engine/)

---

### ブラウザ以外の多くの環境

* Node.jsがサーバーサイドでもインタプリタ言語として動作可能にし、流行った。
(本日はブラウザ上のJavaScriptのみ。)

---

### プロトタイプベースの…

覚えるのが大変なのでまずは忘れていい。

[ES2015/2016+ 記法 個人的メモ](https://qiita.com/romiogaku/items/0f337c489754417f9fa8)

---

[sketck.js](https://p5js.org/get-started/)
```
function setup() {
}

function draw() {
  ellipse(50, 50, 80, 80);
}
```

---

index.htmlを開く(Google Chrome)

---

○が表示されたら成功！

Developer Toolで見るとcanvasが出来ている。
(JavaScriptが読み込まれている。)

---

こんな感じで書けそう

-----○-----○----------○----------
_____↑Bさん↑Aさん_____↑駅

---

1. 道を書く
2. Bさんを書く
3. Aさんを書く
4. 駅を書く

---

### 道を書く

`draw()` に追加
```
// 道
line(0, 100, 200, 100);
```

* x1, y1, x2, y2
* 左上はx, y = (0, 0)
* xは0が左、yは0が上

---

### キャンバスのサイズを決める

どのくらい大きければ十分か？

* 1kmは1000mなので、2000あれば十分。
* 2000では大きすぎるので、1/10にする。
* 1で10mと考える。

---

### Aさん、Bさん、駅を書く

Bさんは0m、Aさんは500m、駅は1500mの位置にあるとする。

---

```
  // Bさん
  ellipse(0, 100, 10, 10);
```

```
  // Aさん
  ellipse(50, 100, 10, 10);
```

```
  // 駅
  ellipse(150, 100, 50, 50);
```

(最初にあったお試しのellipseは消しましょう。)

---

### Aさんを動かす

関数の外に位置を表す変数を定義する。

```
  var x = 0;

  function draw() {
    ...
    // Aさん
    ellipse(x + 50, 100, 10, 10);
    x++;
  }
```

---

### BさんをAさんの1.5倍の速さで動かす

```
  // Bさん
  ellipse(x * 1.5 + 0, 100, 10, 10);
```

---

ぴったり追いついた。

=> コンピュータを使ってシミュレーションした。

---

## オブジェクト指向で再考

---

* Aさんに右に動いて欲しい。
* => moveRight()
* メッセージ・パッシングという。

---

### 具体的な実装

[クラス | JavaScript リファレンス](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes)

---

AさんはBさんより500m進んだところにいる。

```
class Asan {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}
```

適当な場所でインスタンス化

```
var a_san = new Asan(50, 100);
```

---

Aさんに右に動いて欲しい。

```
class Asan {
  ...
  moveRight() {
    this.x++;
  }
}
```

---

```
  function draw() {
    ...
    // Aさん
    ellipse(a_san.x, a_san.y, 10, 10);
    a_san.moveRight();
  }
```

---

オブジェクト指向とは

> すべてはオブジェクトである。
オブジェクトはメッセージの受け答えによってコミュニケーションする。
オブジェクトは自身のメモリーを持つ。
どのオブジェクトもクラスのインスタンスであり、クラスもまたオブジェクトである。
クラスはその全インスタンスの為の共有動作を持つ。インスタンスはプログラムにおけるオブジェクトの形態である。
プログラム実行時は、制御は最初のオブジェクトに渡され、残りはそのメッセージとして扱われる。

https://ja.wikipedia.org/wiki/オブジェクト指向

---

### 次に

Bさんもクラス化。

---

同じ？

```
class Bsan {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  // Bさんは1.5倍
  moveRight() {
    this.x += 1.5;
  }
}
```

---

### YAGNI

`moveRight()` を汎用的に拡張したくなるが、今は不要。

> "You ain't gonna need it"、縮めて YAGNI とは、機能は実際に必要となるまでは追加しないのがよいとする、エクストリーム・プログラミングにおける原則である。

https://ja.wikipedia.org/wiki/YAGNI

---

### KISS

> Keep it simple stupid.

https://ja.wikipedia.org/wiki/KISSの原則

---

### SOLID

> オブジェクト指向プログラミングの分野において、SOLID（ソリッド）とは、ソフトウェア設計の5つの原則を記憶するための頭字語である。これらの原則は、ソフトウェアをより理解しやすく、より柔軟に、よりメンテナナンス性の高いものにするために考案されたものである。

https://ja.wikipedia.org/wiki/SOLID

---

> 単一責任の原則（Single responsibility principle）

1つのクラスは1つだけの責任を持たなければならない。すなわち、ソフトウェアの仕様の一部分を変更したときには、それにより影響を受ける仕様は、そのクラスの仕様でなければならない。

* そのクラスは何を表すものか考えること。
* 例えば、Personが画面にEllipseを描けるのはおかしい。

---

> 開放閉鎖の原則（Open–closed principle）

「ソフトウェアのエンティティは（中略）拡張に対して開かれていなければならないが、変更に対しては閉じていなければならない。」

* インターフェースから先に変更が漏れてはいけない。

---

> リスコフの置換原則（Liskov substitution principle）

「プログラムの中にある任意のオブジェクトは、プログラムの正しさを変化させることなく、そのサブクラスのオブジェクトと置換できなければならない。」詳しくは契約プログラミングも参照。

* 入れ替えても正しいか？

---

> インターフェイス分離の原則（Interface segregation principle）（英語版）

「汎用的な目的のインターフェイスが1つだけあるよりも、特定のクライアント向けのインターフェイスが多数あった方がよりよい。」

* ○ `draw2D(point, point), draw3D(...)`
* × `draw(dimension)`

---

> 依存性逆転の原則（Dependency inversion principle）

「具体ではなく、抽象に依存しなければならない」

* ○ `person.moveRight()`
* × `if (pserson.instanceOf(Bsann)) moveRightHalfDouble()`

---

### GitHubにアップしたら終了です。

---

## Appendix コーディング規約

[Google JavaScript Style Guide (日本語訳)] (http://cou929.nu/data/google_javascript_style_guide/)
Googleが出しているものだけじゃないので、統一されていることが重要。

Java、Python、C#など、各言語探すとあります。

---

## Appendix デザインパターン

[プログラマ歴12年の僕が選んだ「10年経っても役立つ技術書17選」](https://blog.jnito.com/entry/2014/09/29/074949)
デザインパターンは、今では言語機能として一般化されたものも存在します。
知っておくと特に、コードを読むときに、これはこういう処理の仕方を意識したコードなんだな、と理解できるようになります。

以上
