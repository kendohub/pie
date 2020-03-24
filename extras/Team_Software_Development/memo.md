---
marp: true
title: Team Softoware Development
description: Made to lecture in ttc.
url: https://www.ttc-net.co.jp/
---

# 本日は

チーム開発について学びます。
Gitを使った開発フローや、Scrumについて触れます。

---

## Git

まずはGitについて理解しましょう。

* [Pro Git](https://git-scm.com/book/ja/v2) を全部読んでは大変なので

---

### Git略史

[Git略史](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E7%95%A5%E5%8F%B2)

* 便利
* 高速
* 破壊耐性が高い

---

### Gitリポジトリとは？

コミットの集まりです。
それだけ理解していれば全て理解できます。

---

### 使ってみよう

git init
```
mkdir hello_git
cd hello_git
ls -a
git init .
ls -a
  # => 何が変わったか？
```

---

### ステージする

git add
```
vim index.html
git add index.html
```

(中身は次ページ)

---

index.html
```html
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  </head>
  <body>
    <div id="app">
      <p>
        {{ message }}
      </p>
    </div>
  </body>

  <script>
    var app = new Vue({
      el: '#app',
      data: {
        message: 'Hello Vue!'
      }
    })
  </script>
</html>
```

---

### コミットする

```
git commit -m 'Add index page'
```

---

### コミットとは何か？

```
git log -p
```

=> その時点のファイルシステムのスナップショット(ファイルツリーの断面のこと)である。

---

### GitHubにアップしてみましょう

[コマンドラインを使った GitHub への既存のプロジェクトの追加](https://help.github.com/ja/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)

(アカウントがない人は作りましょう。)

([標準の方法(SSH)を使いましょう。](https://help.github.com/ja/github/authenticating-to-github/connecting-to-github-with-ssh) 借りたPCで作成した秘密キーの公開キーをアカウントに登録しても、終了後に登録を削除すれば問題ありません。)

以下ができればOK！
```
git push -u origin master
```

---

### GitHub Flowで開発する

issueを立ててみよう。

issue1: 文字が反転したら面白いな！
issue2: 入力した文字が表示できたらいいな！

---

#### Featureブランチを作成する

あなたは今、issue1に着手しました。

```
git checkout -b reverse-message
```

---

index.htmlを二箇所直した。
```html
  <body>
    <div id="app">
      <p>
        {{ message }}
      </p>
      <button v-on:click="reverseMessage">Reverse Message</button>
    </div>
  </body>
```
```html
  ...
      data: {
        message: 'Hello Vue!'
      },
      methods: {
        reverseMessage: function () {
          this.message = this.message.split('').reverse().join('')
        }
      }
    })
  </script>
```
---

コミットする
```
git diff
git commit -am 'Reversing message is added'
```

---

pushする
```
git push -u origin reverse-message
```

---

PullRequestを立てる

修正内容: メッセージを反転することで今までにない面白さをユーザーが体験できる。

GitHubの自分のリポジトリのページを見ればやり方が分かりますが、[方法はこちら](https://help.github.com/ja/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)

---

#### レビュー

レビューの目的は？

* ACK or NACK

---

#### ここで、別の開発者は、issue2を片付けていた。

```
# 別の開発者になったと思って
git checkout master
git checkout -b show-input-message
```

---

index.htmlを一箇所直した
```html
  <body>
    <div id="app">
      <p>
        {{ message }}
      </p>
      <input v-model="message">
    </div>
  </body>
```

---

push
```
git diff
git commit -am 'Show user input message'
git push -u origin show-input-message
```

PullRequestを立てる

修正内容: 入力したメッセージが表示されるなんて最高。

---

#### 順番にマージしてみましょう

* コンフリクトしますね。

---

#### CLIでは

```
git co master
git merge reverse-message
git merge show-input-message
vim index.html
  # => コンフリクト箇所がどう見えるか？
git add index.html
git merge --continue
git log --graph
  # => コミットの積み重なり方を理解しましょう。
```

---

#### 間違ってコミットしてしまったら？

まずreflogから戻れるので大丈夫です。
```
git reflog
git reset --hard HEAD@{xx}
```

---

### GitFlowとGitHub Flow

実際に、ステージング環境や本番環境を継続してメンテナンスしていくと、ブランチをどのように運用すればいいか考えるタイミングがあります。
そのときに参考にしましょう。

[@ITの参考記事](https://www.atmarkit.co.jp/ait/articles/1708/01/news015.html)

---

### おまけ

[Netlifyなどと連携](https://rightcode.co.jp/blog/information-technology/netlify-github-up)するとこのアプリを世界に公開できます。

---

ここから第二部

---

## Scrum (スクラム) と Agile (アジャイル) の違い

スクラムはフレームワークで、アジャイルは人や組織の在り方です。
まずはアジャイルについて、[アジャイルソフトウェア開発宣言](https://agilemanifesto.org/iso/ja/manifesto.html) から理解しましょう。

---

### アジャイルの在り方

「よりよい開発方法を見つけだそうとしている。」や、
「ソフトウェア開発の実践あるいは実践を手助けをする活動を通じて」から、
ソフトウェア開発に関わる全ての人（ビジネスサイド、開発者サイド）により良い開発手法を見つけ出そうとする活動そのものであることが読み取れます。

「アジャイル宣言の背後にある原則」にもそれが表れていますね。

Agile(俊敏な)という言葉から、「素早く開発」を連想してしまうかもしれませんが、結果的に一側面をとったらそう見える、というだけです。

---

## Scrum (スクラム) と XP (エクストリームプログラミング) の違い

XPも、スクラムも、「アジャイル開発手法」などと一緒くたに言われていますが、それぞれ異なります。
どちらも開発のためのフレームワーク(手法)です。
XPは方法論寄りで、スクラムは組織論寄りのフレームワークです。
そのため、XPの手法の一部(例えばペアプログラミング)をスクラムで使う、と言ったことが可能です。

今回は、スクラムを取り上げます。

([XPの概要はここなど](https://slide.meguro.ryuzee.com/slides/96))

---

## スクラムとは？

実践するときは、[スクラムガイド](https://www.scrumguides.org/scrum-guide.html) を読んで理解しましょう。

=> [日本語版PDF](https://www.scrumguides.org/docs/scrumguide/v2017/2017-Scrum-Guide-Japanese.pdf)

---

### スクラムとは？(ガイドから抜粋)

スクラムは、1990 年代初頭から複雑なプロダクトの作業管理に使用されてきたプロセスフレームワークである。

プロダクトを構築するプロセス、技法、決定的な方法論などではない。さまざまなプロセスや技法を取り入れることのできるフレームワークである。

スクラムフレームワークは、スクラムチームとその役割・イベント・作成物・ルールで構成されている。それぞれに目的があり、スクラムの成功や利用に欠かせない。

---

### スクラムとは？その2

スクラムの本質は、少人数制のチームである。個々のチームは非常に柔軟で適応力に優れている。
こうした強みは、単一のチームであっても、複数あるいは多数のチームであっても、数千人の成果やプロダクトを開発・リリース・運用・保守するネットワーク型のチームであっても有効である。
チームは協力や情報交換をしながら、洗練された開発アーキテクチャやターゲットとするリリース環境を整えていく。

スクラムガイドで「開発」や「開発する」といった言葉が登場するとき、それは上記のような複雑な作業を意味している。

---

### スクラムの概要を1分で

スクラムガイドの用語が関連図にまとまっています。

[スクラムの概要を1分で理解できるイラスト](https://www.ryuzee.com/contents/blog/7124)

---

### 実践は難しい

スクラムガイドより

* 作生物の透明性：いつでも価値の最大化やリスク制御をする判断ができること
* 「完成（Done）」の定義：全員が完成の意味を理解していること

Ryzeeさんより

* [スプリント1を始める前にどんな準備をするか](https://www.ryuzee.com/contents/blog/7147)

---

## 結局大事なことは

ツールでも技法でも、先にあるのは「より良くしよう」と言う思いです。

---

## 以上

書いたコードはGitHubにアップされているので終了です。
