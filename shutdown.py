import os
import sys
import time

dir = os.path.dirname(os.path.abspath(__name__)) # スクリプトのあるディレクトリの絶対パスを取得
exist = 1

# ------ ダウンロード中のファイルがなくなるまでループ ---------
while exist >= 1:
    exist = 0
    for file in os.listdir(dir):
        base, ext = os.path.splitext(file)
        if ext == '.crdownload':
            exist += 1
            print("File is founded")
            filename = base + ext
    print("Waiting...")
    time.sleep(30)

os.system('shutdown -s -f')