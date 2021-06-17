import os
import sys

for f in sys.argv[1:]:
    f = f.replace(" ", "\ ")
    print("対象のファイルパス:", f)
    print("パーミッションを変更中...")
    print("ディレクトリのパーミッションを書き換え中...(場合によっては時間がかかります)")
    os.system("find " + f + " -type d -exec chmod 777 \{\} \;")
    print("ディレクトリのパーミッション変更完了！")
    print("ファイルのパーミッションを書き換え中...(場合によってはすごく時間がかかります)")
    os.system("find " + f + " -type f -exec chmod 777 \{\} \;")
    print("ファイルのパーミッション変更完了")
    print("パーミッション変更完了！")

print("chmod process finished :)")
