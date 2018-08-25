import os
import sys
import time

dir = os.path.dirname(os.path.abspath(__name__)) # スクリプトのあるディレクトリの絶対パスを取得
exist = 0

# ------ ダウンロード中のファイルを探す -------
for file in os.listdir(dir):
    print(file)
    base, ext = os.path.splitext(file)
    if ext == '.crdownload':
        exist = 1
        print("File is founded")
        filename = base + ext

# ------ ファイルがなくなるまでループ ---------
while exist == 1:
    print("Waiting...")
    time.sleep(2)
    if not os.path.exists(dir + "\\" + filename):
        exist = 0

os.system('shutdown -s -f')