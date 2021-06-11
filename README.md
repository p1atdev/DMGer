# DaMaGe
Bypass restricting DMG file extracting...
制限マックのDMGが解凍できないという制限を回避することができます

# Requirements
- Python 3
- 7zip
- 動くターミナル

# How to use
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

# License
手法の発見者、著作者はME氏にあります。
本人の意思により、使用に関しては完全にフリーです。どんどん配布しても構いませんが、それによって発生した損害などについてはME氏、Plat共に責任を負いません。