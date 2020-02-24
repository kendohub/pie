---
marp: true
title: Programming Language C++
description: Made to lecture in ttc.
url: https://www.ttc-net.co.jp/
---

# 本日は

C++についての概要を学びます。

```
# gccがない人は入れましょう。
gcc --version
sudo apt install -y build-essential
```

---

## プログラミング言語としての大体の分類

C++（シープラスプラス）は、汎用プログラミング言語のひとつである。派生元であるC言語の機能や特徴を継承しつつ、表現力と効率性の向上のために、手続き型プログラミング・データ抽象・オブジェクト指向プログラミング・ジェネリックプログラミングといった複数のプログラミングパラダイムが組み合わされている。

[Wikipedia](https://ja.wikipedia.org/wiki/C%2B%2B) より。

---

## 特徴

Cに対して今では当たり前となった機能を多く取り入れてきた言語

* C言語を、より大規模開発に適するように拡張、改善したもの。
* (多重)継承、カプセル化、多態性、などのオブジェクト指向プログラミングが可能。
* テンプレートを使った抽象化が可能。動的な型に対して処理の記述が可能。コンパイル時に型が解決される。
* STLなど標準ライブラリによって、イテレーション、線形リストなど一般的な表現がサポートされている。
* 演算子をオーバーロードできる。
* 例外をthrowできる。

---

## 作者

[ビャーネ・ストラウストラップ](https://ja.wikipedia.org/wiki/%E3%83%93%E3%83%A3%E3%83%BC%E3%83%8D%E3%83%BB%E3%82%B9%E3%83%88%E3%83%AD%E3%83%B4%E3%82%B9%E3%83%88%E3%83%AB%E3%83%83%E3%83%97)

---

## インストールコマンド

Ubuntu
```
sudo apt install -y build-essential
```

Mac
```
# Xcodeと一緒に入っているはず
```

---

## Hello World

Hello.cpp
```
#include <iostream>
using namespace std;
int main(void)
{
  cout << "Hello, World!\n";
  return 0;
}
```

C++のコンパイルと実行
```
g++ -o Hello Hello.cpp
./Hello
```

---

## STL

* オブジェクトの入れ物をコンテナと呼びます。
* コンテナの要素にアクセスするにはイテレータを使います。
* コンテナをソートしたりコピーしたり探索したりするアルゴリズムが提供されています。
* 関数呼び出し演算子("()"のこと。operatorと言う。)をオーバーロードしたオブジェクトを作れます。
* [難解さがあります。](https://ja.wikipedia.org/wiki/Standard_Template_Library)

---

## Boost

Boostと言うライブラリがあります。
様々な便利機能や、数学ライブラリなどを提供しています。
C++の最新仕様を策定する機関になっています。

---

## ポインタ

Cのようにハードウェアに近い層でのプログラミングができます。
つまり、メモリ管理を自分ですることができます。
Cの機能ですが、メモリへの参照をポインタと言います。
C++でもよく使うので紹介します。

---

### サンプルコード

```
#include <iostream>
using namespace std;
int main(void){
    int a[] = {1, 2, 3, 4};
    int *b = a;
    cout << *b;
    cout << *b+1; // *(b+1)
    cout << *++b; // *(++b)
    return 0;
}
```
* int型の変数4つ分の領域を静的に確保する。(a)
* int型のポインタ要の領域を確保して、aを指させる。(b)
* bの指しているところから値を読み取って、coutに出力する。(*b)
* bの指しているところの次の位置から値を読み取って、coutに出力する。(*b+1)
* bをbの次の位置に移動して、bの指しているところの値を読み取って、coutに出力する。(*++b)

---

### こうしたらどうなる？

```
#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int a[] = {1, 2, 3, 4};
    int *b = a;
    cout << *b;
    cout << *b+1; // *(b+1)
    cout << *++b; // *(++b)
    cout << *++b; // *(++b)
    cout << *++b; // *(++b)
    cout << *++b; // *(++b)
    return 0;
}
```

* 読み取ってはいけない場所が読み取られるかも。

---

### メモリ管理

先の例では、メモリを静的に確保できる。
ネットワークやファイルからどれだけのデータをメモリに読み込まないといけないかは事前に分からない。
メモリを動的に確保する必要もある。(malloc, freeなどの用語が出てくる)
コンピュータというハードウェアを操作しているので、我々には制約がある。
そのため、計算量(時間計算量、空間計算量)を見積もる必要がある。

* [(参考) ポインタ虎の巻](http://www.nurs.or.jp/~sug/soft/tora/tora1.htm)

---

## 以上

GitHubにアップしたら終了です。

---

## インストールコマンド

Ubuntu
```
sudo apt install -y build-essential
```

Mac
```
# Xcodeと一緒に入っているはず
```
