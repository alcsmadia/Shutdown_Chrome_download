import os
import sys
import time

dir = os.path.dirname(os.path.abspath(__name__)) # スクリプトのあるディレクトリの絶対パスを取得
exist = 0

while exist == 0: # n個ファイルダウンロードしてるときn回ループ
    # ------ ダウンロード中のファイルを探す -------
    for file in os.listdir(dir):
        base, ext = os.path.splitext(file)
        if ext == '.crdownload':
            exist = 1
            print("File is founded")
            filename = base + ext
    if exist == 0:
        print("Download file is not founded")
        time.sleep(20)
        os.system('shutdown -s -f')
        sys.exit() # 終了

    # ------ ファイルがなくなるまでループ ---------
    while exist == 1:
        print("Waiting...")
        time.sleep(30)
        if not os.path.exists(dir + "\\" + filename):
            exist = 0