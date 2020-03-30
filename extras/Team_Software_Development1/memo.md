---
marp: true
title: Team Softoware Development1
description: Made to lecture in ttc.
url: https://www.ttc-net.co.jp/
---

# 本日は

チーム開発について学びます。
そのために重要な、Gitを使った開発フローについて学びます。

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

## 以上

書いたコードはGitHubにアップされているので終了です。
