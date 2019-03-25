import os
import time

# ------ ダウンロード中のファイルがなくなるまでループ ---------
while True:
    print("Waiting...")
    
    n = 0
    for file in os.listdir():
        base, ext = os.path.splitext(file)
        if ext == '.crdownload':
            n += 1
            time.sleep(30)
    
    if n == 0:
        break

os.system('shutdown -s -f')