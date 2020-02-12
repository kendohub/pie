---
marp: true
title: Programming Language Java
description: Made to lecture in ttc.
url: https://www.ttc-net.co.jp/
---

# 本日は

Javaの仕組みと開発手法を学びます。

---

## プログラミング言語としての大体の分類

Java言語はC++に類似した構文のプログラミング言語であり、オブジェクト指向が主要パラダイムとして導入されている。

Javaは、従来のソフトウェアが抱えていた移植性問題の解決を図り、特定の環境に依存しない理想的なクロスプラットフォーム・プログラムの実現を目指して開発された。
Javaソフトウェアは、家電機器や乗用車の組み込みシステムから、マイクロ制御装置、携帯機器、パーソナルコンピュータ、サーバーマシン、スマートカード、スマートフォンといった様々な環境に普及している。

[Wikipedia](https://ja.wikipedia.org/wiki/Java) より。

---

### JavaとOracle

Javaは1995年にサン・マイクロシステムズ(Sun Microsystems)から発表された。
2010年にOracleがSunを買収して権利を取得した。
この時MySQLやSolarisの権利もOracleに移った。

---

### 特徴

* Javaのソースコードはバイトコードにコンパイルされる。(*.classファイルはそれ)
* JavaのバイトコードはJava Virtual Machine (JVM) 上で動作する。
* JVMがマルチプラットフォームをサポートしている。ので、ソースコードはクロスプラットフォームになる。
* JVMがメモリ管理(GC)を行ってくれる。JavaのチューニングでヒープやGCという言葉が出てくるのはこの仕組みの中の話。

---

### インストール

Ubuntu
```
sudo apt update
sudo apt install -y default-jdk
java -version
```

Mac
```
brew cask install java
java -version
```

※PATHが通ってなかったら通す。
※Windowsの場合、JAVA_HOMEという環境変数が必要だったりそうじゃなかったりする。

---

### OpenJDK

*OpenJDKはオープンソースコミュニティが開発するJDK*

OpenJDK (Open Java Development Kit) は、Java Platform Standard Edition (Java SE) のオープンソース実装です。
アップストリームコミュニティー プロジェクト OpenJDK は現在、Oracle がスポンサーおよび主導 しており、リンク例外ありの GNU 一般公衆利用許諾書 (GNU GPL 2 および 2+) でリリースされています。

OpenJDK は、Red Hat Enterprise Linux の Java Development Kit (JDK) および Java Runtime Environment (JRE) です。

[RedHat; OpenJDK のライフサイクルおよびサポートポリシー](https://access.redhat.com/ja/articles/1457743) より。

---

### Oracle JDK

*Oracle JDKはOracleが開発するJDKで、有償化された*

Oracle JDK のライセンスに関する重要な変更

2019年4月16日のリリースより、Oracle JDKのライセンスが変更されました。
新しいライセンス、Oracle Technology Network License Agreement for Oracle Java SEは、これまで提供してきた過去のバージョンのJDKのライセンスと大きく異なります。
新しいライセンスでは、個人での利用や開発での利用などには無償で使用できます。
しかし、以前のOracle JDKライセンスで許可されていたその他の目的には使用できなくなっている可能性があります。
これらの製品をダウンロード、使用する前にライセンスの内容を十分にご確認ください。

[Oracle; Java SE ダウンロード](https://www.oracle.com/technetwork/jp/java/javase/downloads/index.html) より。

---

#### OpenJDKとOracle JDKまとめ

* 2020年時点ではOpenJDKがオープンソースライセンスで利用できる。
* 以上。

---

### JDKとJRE

Java Development Kit (JDK) は開発用、Java Runtime Environment (JRE) は実行用の環境。
JVMはどちらでもインストールされる。
JDKはJavaの開発ツールもインストールされる。

---

### Java SEとJava EE

SEはStandard Edition、EEはEnterprise Edition。
Java SEは、Javaの文法を覚えたら書ける範囲の内容。標準ライブラリ(JavaではAPIと呼ぶ)も含む。
Java EEは、より豊富な機能を持ったライブラリを使って開発をするための仕組みと、その実行環境を指す。
Java EEを使った開発は、JDKをインストールしただけではできない。
例えば、Java Servlet APIに関するライブラリはJDKに含まれないので、Tomcatが提供するライブラリを使った開発と、Tomcatでの実行が必要となる。
Tomcat以外でも、GlassFishやWildFly、それらの商用版などを使っても同様にできる。

---

### Java SEのAPIの範囲

* [Java8まで](https://docs.oracle.com/javase/jp/8/docs/api/)
* [Java11](https://docs.oracle.com/javase/jp/11/docs/api/index.html)
  * Java9で導入されたJigsawにより、モジュール化されている。
  * Java8から廃止されたパッケージや、パッケージ名が変わったものがある。

---

### Tomcatとは何か

The Apache Tomcat® software is an open source implementation of the Java Servlet, JavaServer Pages, Java Expression Language and Java WebSocket technologies. The Java Servlet, JavaServer Pages, Java Expression Language and Java WebSocket specifications are developed under the Java Community Process.

[Apache Tomcat](http://tomcat.apache.org/)

* Java EEのWebアプリケーション周りの仕様を実装したもの。Java Servletも含まれている。その実行環境も兼ねる。
* JavaのWebアプリケーション開発はServlet/JSPから主流になったので、JavaのWebアプリケーションといえばTomcatで動かす、という時代があった。(いつ？)
* Java EEでは、例えばJava Servletを動かす機能を指して、サーブレットコンテナと言う。EJBコンテナとか、何々コンテナという用語はよく登場する。

---

### Tomcat以外のJava EE実行環境

* RedHat系 - JBoss EAP、WildFly
* Oracle系 - WebLogic、GlassFish
* 基本的に、Tomcat以外は、Java EEの全機能を実装している。
* アプリケーションサーバーと呼ばれることもある。
* 他にもIBMとか様々存在する。

---

### Java EEの仕組み

例えば、なんとかServletクラスを継承して、リクエストを処理するコードを書くだけで、簡単なWebアプリケーションが作れる、といったことはどのように実現されているのか？

* Tomcatなどが実行されると、初期化処理が設定ファイルなどにしたがって行われる。その中で、Servletコンテナも初期化される。(Servletの場合、web.xmlの設定に従う。)
* web.xmlの設定にしたがって、開発者の書いたクラスがClass Pathから読み込まれる。
* Servletコンテナが、リクエストを受け付けると、設定にしたがって対象のクラスのオブジェクトに受け渡す。

Java EEを実装した実行環境が、うまく環境を整えてくれて、簡単にアプリケーションが書けるようになっている。EJBなら、WildFlyがEJBコンテナの役割を担ってDIしてくれるなど。

---

### Java EE関連のフレームワーク

Webアプリケーション開発のためのフレームワークは、自然淘汰されて、2020年にはSpringが生き残っている。
これらのフレームワークは、Java EEの機能をラップして、より使いやすくすることで発展した。
使いやすくした機能がJavaに逆輸入されることもあった。(JSFなど)

---

### Javaの機能拡充の仕組み

JavaのAPIはJava Community Process (JCP)で提案、実装、レビューが行われ、機能が拡充されている。
[JCPのJSRの例](https://ja.wikipedia.org/wiki/Java_Community_Process)

Java EEでWebアプリケーションを開発するときによく使われるEJB、Servlet/JSP、JAX-RS、JSFなども同様。
それぞれのAPIにバージョンがあり、それらをある程度まとめて、Java SEいくつとか、Java EEいくつといったバージョンで括られる。

---

### Javaアプリケーション開発手法

Javaのアプリケーションは、基本的にはIDEを使って開発します。

* Eclipse
  * オープンソースライセンスで普及率が高い。プラグインも多数。
* NetBeans
  * 一時期流行ったが開発が止まってる？
* IntelliJ
  * 安定のJetBrains製品。JetBrainsは他の言語向けIDEを多数出している。
* Android Studio
  * IntteliJベース。Androidアプリは標準の開発環境がJava。

---

### Javaアプリケーションのビルド

`*.java` ファイルは、Javaコンパイラでバイトコードにコンパイルして、 `*.class` ファイルにします。
`*.class` ファイルを一つにまとめるためにZIPアーカイブしたものが、 `*.jar` ファイルです。
Webアプリケーション用の階層構造が定められている `*.war` ファイルも同様です。
これらを一つ一つコンパイルしてアーカイブするのは面倒なので、「ビルド」という手順は自動化されています。
IDEで「ビルド」を実行すると、指定の形式で出力してくれます。
CLIでは、Ant、Maven、Gradleなどのツールが発達しました。

---

### Javaアプリケーションのデプロイ

ビルドの出力ファイルは、アプリケーションサーバーに配置して、実行します。
もちろん、Javaなので、 `java -jar` コマンドで実行することもできます。
アプリケーションサーバー自体も、多くはjavaコマンドで起動されています。
(TomcatのWindowsネイティブ実装などもありますが例外的です。)

---

### Javaの実行

`java <main関数のあるクラス名>` が最小の実行コマンドです。
指定されたクラスの、 `public static void main()` が実行されます。
実行ディレクトリ以外のクラスを読み込みたい場合は、Class Pathを指定します。
どんなに複雑なJavaアプリケーションでも、基本はこれです。
アプリケーションサーバーのログや起動設定などを読むと、理解が進むと思います。

---

### 実行してみる

Hello.java
```
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

コンパイル
```
javac Hello.java
```

実行
```
java Hello
```

---

### ヒープの確認など

Hello.java
```
public class Hello {
    public static void main(String[] args) {
        String s = "";
        for (int i = 0; i < 6000; i++) {
            s += "Hello, world!";
            System.out.println(s);
        }
    }
}
```

```
javac Hello.java
java Hello
jstat -gcutil -h10 <PID> 1000
```

---

### 以上

GitHubにアップしたら終了です。

---

### Appendix: その他のJVM利用言語

* Groovy
* Scala
* Kotlin
* Clojure

---

## インストールコマンド

Ubuntu
```
sudo apt update
sudo apt install -y default-jdk
java -version
```

Mac
```
brew cask install java
java -version
```
