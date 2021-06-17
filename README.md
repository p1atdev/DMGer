# DMGer
Bypass restricting DMG file extracting...
制限マックのDMGが解凍できないという制限を回避することができます

# Requirements
- Python 3
- 7zip
- 動くターミナル

# 注意
中で使用されている7zipのコマンドは環境によって異なるので、各自変更してください

# ToDo
- 環境の7zipコマンドを尋ねて自動で変更できるように

# How to use :extraction.py & chmod.py
ターミナルで`extract.py`を以下のように実行します
```bash
python3 /path/to/extract.py /path/to/googlechrome.dmg
```
すると`~/Downloads`フォルダに解凍済みのフォルダが作成されます。
この時点ですでに.appファイルも作成されますが、実行できないので`chmod.py`を以下のように実行します

```bash
python3 /path/to/chmod.py /path/to/extraced.app
```
するとアプリが起動できるようになります。

このあとは自由に名前を変えたり自分の好きなフォルダに移したりしちゃいましょう！

# How to use: dmger.py
以下を実行
```
python3 dmger /path/to/yourdmg.dmg
```
超簡潔！

# License
手法の発見者、著作者はME氏にあります。
本人の意思により、使用に関しては完全にフリーです。どんどん配布しても構いませんが、それによって発生した損害などについてはME氏、Plat共に責任を負いません。
