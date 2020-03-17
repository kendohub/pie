---
marp: true
title: Network and Security
description: Made to lecture in ttc.
url: https://www.ttc-net.co.jp/
---

# 本日は

ネットワークとそのセキュリティについて学びます。

[Docker Playground](https://labs.play-with-docker.com/) を使います。

Dockerのチュートリアルは、[Play with Docker Classroom](https://training.play-with-docker.com/) が分かりやすいです。

---

## Webアプリケーションでよく使う通信プロトコル

HTTP
SSL/TLS
TCP/IP
PPP
802.3 (Ethernet), 802.11a/b/g/n

---

### OSI参照モデル

先程のプロトコルの分類モデル。
Open Systems Interconnectionという規格のために定義されたが、規格は普及せず、定義だけ普及した。
一般的なプロトコルは別にOSI参照モデルに従って分類されるわけではないが、階層化されているので分かりやすい面もある。

[OSI参照モデル](https://ja.wikipedia.org/wiki/OSI参照モデル)

---

### 通信とは？

コンピュータ間のデータのやり取り。

---

### ネットワークとは？

通信できるコンピュータの集まり。
コンピュータ間で通信できると便利。

---

### インターネットとは？

ネットワーク間を相互に広く接続したネットワーク。
国際的にオープンなネットワーク。

インターネットに対して、社内ネットワークなどの、内側のネットワークをイントラネットと呼ぶ。

---

### パブリックネットワークとプライベートネットワーク

誰でも参加できるネットワークが、パブリックネットワーク。
認められたもの(コンピュータ)だけが参加できるのが、プライベートネットワーク。

* 社内LANは？
* 公衆Wi-Fiは？

---

### LANとWAN

Local Area Network(LAN)とWide Area Network(WAN)。これも範囲の違いがあるだけ。
LANは、あるネットワーク機器の内側のネットワークを指す。
WANはその外側のネットワークを指す。

---

### ネットワーク機器

*(スイッチング)ハブ*

特定のコンピュータにデータを送信するもの。L2スイッチ。

*ルーター*

別のネットワークにデータを送信するもの。L3スイッチ。
インターネットとの間にあるルーターを、インターネットゲートウェイ(IGW)と呼ぶ。

---

## 実際にネットワーク上の通信を見る

Dockerで通信を見てみましょう。

[Docker Networking Hands-on Lab](https://training.play-with-docker.com/docker-networking-hol/) を開きます。

* Docker用の仮想マシンが右側に2台あります。便利ですね。

---

### bridge

```
docker network ls
docker network inspect bridge
  # => SubnetとGatewayが表示されたと思います。
```

* Subnet: 自分の所属するネットワークを識別する単位です。
* Gateway: ルーターのIPアドレスです。
* bridge: 別のネットワークとの橋渡しをする物です。Dockerのbridgeは、これから起動するDockerコンテナと、Dockerを実行している仮想マシンとの橋渡しをしている物です。コンテナも一つの仮想コンピュータなので、きちんと仮想のネットワークインターフェースを介して通信します。

---

### bridgeの定義

bridgeが、仮想マシン自体にどう定義されているかを見てみます。

```
apk update
apk add bridge
brctl show
  # => docker0という名前のbridgeが定義されている。
ip a
  # => docker0というbridgeが一つのネットワークインターフェースになっている。
```

---

### Dockerコンテナを起動

```
docker run -dt ubuntu sleep infinity
docker ps
brctl show
  # => vethと接続されている。
ip a
  # =>
```

---

### コンテナのIPアドレスの確認

```
docker network inspect bridge
```

先ほど起動したDockerコンテナにIPアドレスが振られていることが確認できます。

このコンテナは停止しましょう。
```
docker ps
  # => コンテナIDを控える
docker stop <yourcontainerid>
```

---

### NAT

Network Address Translation(NAT)を使って、Dockerコンテナ上のTCP80ポートに、仮想マシンの8080ポートからアクセスしてみます。

```
docker run --name web1 -d -p 8080:80 nginx
curl localhost:8080
```

[Docker Playground](https://labs.play-with-docker.com/) でも、上記のコマンドを試せます。
(Template -> One Manager, One Workerで上記の環境を再現できる。)

---

## ネットワークのセキュリティ

先ほどのコンテナのTCP8080ポートに、自分のブラウザからアクセスできますか？

* 相当頑張っても無理です。

---

### では、セキュリティとは？

自分のWebサイトにアクセスして欲しいなら、インターネットから先ほどのTCP8080ポートまでのルートを、作る必要があります。
ネットワーク機器を設定して、今度は、仮想マシンからインターネットに出るbridgeを定義します。
それだけでは、インターネットから仮想マシンを見つけられません。
インターネットゲートウェイが持つグローバルIPアドレスなら見つけられるので、そこから仮想マシンまで、NATでデータを中継します。
だいぶ端折りましたが、これでようやく、仮想マシンのWebサイトにアクセスできます。

同時に、セキュリティについて考える必要が出てきます。

---

### TCP8080ポートのセキュリティ

TCP8080ポートは、NginxがLISTENしています。
Nginxの脆弱性があれば、その影響を受けます。
また、NginxがWebアプリケーションとのゲートウェイ(この場合は、リバースプロキシなど)になっている場合、Webアプリケーションの脆弱性対策ももちろん必要です。

---

### それ以外のセキュリティ

仮想マシンに直接ログインされたらどうしようもありません。
直接端末からログインする以外には、例えば、sshは、設定を変えなければデフォルトでTCP22ポートを使います。
先ほどのネットワーク機器の設定で、仮想マシンのTCP8080ポートだけでなく、TCP22ポートにアクセスできるようになっていたら、侵入を試みられてしまいます。
(もちろん、TCP8080ポート以外は誰もLISTENしていないのであれば、そのようなことにはなりませんが。)

※なお、LISTENとは、TCPの用語です。プログラム上は、TCPソケットを監視する無限ループのことです。

---

### 通信の暗号化

HTTPではログインできなくしているWebサイトも多数ありますね。
ネットワークの仕組み上、盗聴は避けられません。
パスワードだけでなく、ログイン後の通信も盗聴されてしまえば、なりすましが可能です。
そのため、常に暗号化通信方式(HTTPなら、TLS)を使用しているか確認しましょう。

---

## 便利なコマンド

traceroute
```
apt update
apt install -y traceroute
traceroute --tcp www.github.com
```

dig
```
apt install dnsutils
dig www.github.com
```

---

## OSI参照モデル おさらい

[OSI参照モデル](https://ja.wikipedia.org/wiki/OSI参照モデル) のイメージが変わったでしょうか？
疑問に思ったら、都度調べていくと理解が深まります。

---

## 以上

historyコマンドの履歴をGitHubにアップしたら終了です。

今回使ったDockerのトレーニングサイト、分かりやすいです。
[Play with Docker Classroom](https://training.play-with-docker.com/)
