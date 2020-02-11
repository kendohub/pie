---
marp: true
title: Computing
description: Using Go. Made to lecture in ttc.
url: https://www.ttc-net.co.jp/
---

# 本日は

プログラミング言語の学び方を横に広げて、Goを学びます。

---

## プログラミング言語としての大体の分類

Goは、静的型付け、C言語の伝統に則ったコンパイル言語、メモリ安全性、ガベージコレクション、構造的型付け、CSPスタイルの並行性などの特徴を持つ。Goのコンパイラ、ツール、およびソースコードは、すべてフリーかつオープンソースである。

[Wikipedia](https://ja.wikipedia.org/wiki/Go_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E)) より。

---

## 作者

[2009年、GoogleでRobert Griesemer、ロブ・パイク、ケン・トンプソンによって設計された。](https://ja.wikipedia.org/wiki/Go_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E))

---

## 特徴

軽量スレッディングのための機能、Pythonのような動的型付け言語のようなプログラミングの容易性、などの特徴もある。Go処理系としてはコンパイラのみが開発されている。マスコット・キャラクターはGopher（ホリネズミ）。

---

## Hello World

Go言語 検索
それらしいページを探す。

---

TOPページにインタプリタがあり、Hello Worldできます。
なんとなく読めると思います。

---

## Getting Started

まずはインストール。
https://golang.org/doc/install

---

### インストール

Windows WSLのUbuntuの場合は、Linuxのインストール方法に従う。

が、 ubuntu apt install go で検索してみる。

---

親切にもリポジトリを用意してくれていた。

```
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt-get update
sudo apt-get install golang-go
```

[GitHubのWikiにある。](https://github.com/golang/go/wiki/Ubuntu)

Macの場合は

```
brew install go
```

---

公式のインストール方法は何だったの？

最新版のバイナリを直接手に入れたいのであれば使いましょう。
それ以外の場合はリポジトリの管理者を信用できるなら使いましょう。

---

## チュートリアルをやってみる

[Learning Go](https://golang.org/doc/#learning)

A Tour of Go の日本語訳を見つけましょう。
とても分かりやすいのでそのまま使います。

```
mkdir -p work/go
cd work/go
```

---

### Packages, variables, and functions.

Goはパッケージという単位でモジュールを管理します。

### Flow control statements: for, if, else, switch and defer

deferでtry-catch-finallyのfinallyようなことをするのが特徴的です。

### More types: structs, slices, and maps.

覚える型は多くありません。

### Methods and interfaces

オブジェクト指向のクラスはありません。

### Concurrency

goroutineでコンピュータリソースを最大限使用できます。

---

## ここまでで

Goの概要は掴めましたか？

---

### 実用的には

C/C++より書きやすい。
並行処理が標準機能。
C/C++に近いパフォーマンス。

とは言っても、書きやすさは今日学んだ通りなので、
読み書きしやすい言語では手の届かない処理が出てきた時の選択肢として取っておいてください。
なお、UNIX、LINUXだけでなく、Android、iOS、WebAssemblyもサポートし始めました。

---

# もっと使ってみよう

Pythonとの違いを見るために、Webシステムを考えましょう。

---

## 問題(イントロダクションより再掲)

AさんとBさんは同僚で、同じ道沿いに住んでいます。
毎日その道を通って、駅から会社に一緒に向かいます。
AさんはBさんよりも駅に近く、駅から1km。Bさんは1.5kmの位置に住んでいます。
ある日、いつもBさんが来る時間にAさんが家の前で待っていると、寝坊をしたBさんから連絡がありました。
「寝坊した！今から家を出る！走って追いつくから、先に行ってて！」
BさんがAさんに追いつくには、いつもよりどれだけ早く走らないといけないでしょうか？

---

## まずはWebアプリの書き方

[Writing Web Applications がちゃんとあります](https://golang.org/doc/articles/wiki/)

* Introducing the net/http package (an interlude) を見つけましょう。
* wiki.goに保存してビルドすると実行できます。

```
go build wiki.go
./wiki
```

---

## AさんとBさんをプログラム化する

AさんとBさんは家から駅まで一本道を進む
Aさんが1km進むまでに、Bさんが1.5km進めば良い

-----Bさん-----Aさん----------駅----------

---

### Aさんの動きを実装

wiki2.go
```
func handler(w http.ResponseWriter, r *http.Request) {
	for i := 0; i <= 150; i++ {
		fmt.Fprintf(w, "%d\n", r.URL.Path[1:])
	}
}
```

ビルドして実行
```
go build wiki2.go
./wiki2
```

---

### Bさんの動きも実装

wiki3.go
```
func handlerA(w http.ResponseWriter, r *http.Request) {
	for distance := 50; distance <= 150; distance++ {
		fmt.Fprintf(w, "%s: %d\n", r.URL.Path[1:], distance)
	}
}

func handlerB(w http.ResponseWriter, r *http.Request) {
	for distance := 0.0; distance <= 150.0; distance += 1.5 {
		fmt.Fprintf(w, "%s: %.1f\n", r.URL.Path[1:], distance)
	}
}

func main() {
	http.HandleFunc("/a_san", handlerA)
	http.HandleFunc("/b_san", handlerB)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

---

### Pythonの実装と比べてどっちが正解か？

---

### Goの動きをもう少し知る

Apache Benchをインストール

```
sudo apt install apache2-utils
```

Macの場合はもう使えないのでHeyにする

```
brew install hey
```

---

### Bさんにスリープを入れてみる

```
import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func handlerB(w http.ResponseWriter, r *http.Request) {
	for distance := 0.0; distance <= 150.0; distance += 1.5 {
		fmt.Fprintf(w, "%s: %.1f\n", r.URL.Path[1:], distance)
	}
	time.Sleep(5000 * time.Millisecond)
}
```

---

### 負荷を掛ける

```
ab -c 1000 -n 1000 http://localhost:8080/b_san
```

htopでプロセスの状態を確認する
```
htop
```

この状態でAさんにアクセスできるか？

---

### PythonにもSleepを入れて比較してみよう

```
import time
time.sleep(5)
```

htopでプロセスの状態を確認する
```
htop
```

---

### 結果

Goはスレッド数が増えない。
Flaskでは、それがスレッド単位になるので、1アクセスに対して1スレッド生成されている。
Goの方がSleep時間とほぼ同一の応答時間。goroutineが上手く働いてCPUの空きをスムーズに割り当てられているのでは。

---

### 以上

GitHubにアップしたら終了です。

goroutineの並行処理の強力さが見られましたね。

---

## インストールコマンド

Ubuntu
```
# Go
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt-get update
sudo apt-get install golang-go
# Apache Bench
sudo apt install apache2-utils
```

Mac
```
# Go
brew install go
# Apache Benchの代わり
brew install hey
```
