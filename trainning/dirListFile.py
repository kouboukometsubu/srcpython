import glob
import os

# Headerファイルのみを取得
files = glob.glob("D:\srcfile\AltaxV4Comm\Std\DLLTools\StdClass\cpphtools\*.h")

#ファイル名だけを出力
for file in files:
    filename = os.path.basename(file)
    print(filename)
