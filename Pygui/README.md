# PySimpleGui

# EXE化
pip install PyInstaller
pyinstaller -wF main.py  # importエラー
pyinstaller main.spec --onefile  # .specファイルに追記を行った後にコマンドを実行しimportエラー解消

## 参考
[Pythonでも簡単にGUIは作れる](https://qiita.com/konitech913/items/61dc715ddaad54505a29)  
[Pyinstallerを使ってPythonコードから生成した実行ファイルについて、実行時エラーModuleNotFoundErrorを回避](https://qiita.com/kanedaq/items/e65507878c52ad67d002)  
