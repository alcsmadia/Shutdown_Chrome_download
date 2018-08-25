import os
import sys
import time

dir = os.path.dirname(os.path.abspath(__name__)) # スクリプトのあるディレクトリの絶対パスを取得

# ------ ダウンロード中のファイルがなくなるまでループ ---------
while True:
    time.sleep(30)
    n = 0
    for file in os.listdir(dir):
        base, ext = os.path.splitext(file)
        if ext == '.crdownload':
            n += 1
            print("File is founded")
            filename = base + ext
    print("Waiting...")
    if n == 0:
        break

os.system('shutdown -s -f')