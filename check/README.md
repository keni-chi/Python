# Python

## 概要
覚書である。順次記載予定。

## 詳細
pep8 flake8 pycodestyle スタイルガイド  
pep257 pydocstyle  
flake8はpep8に加えて論理エラーの検出も行う。  

## 手順
pip install flake8  
pip install flake8-docstrings  
flake8 xxxxx.py  

pip install autopep8  
pip install autoDocstring  
autoDocstringのプラグインをインストール  

### setting.json
{
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "python.linting.lintOnSave": true,
    "python.linting.pylintEnabled": false,
    "python.linting.pep8Enabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--ignore=W293, W504",
        "--max-line-length=150",
        "--max-complexity=20"
    ],
    "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": [
        "--aggressive", "--aggressive",
    ],
    "autoDocstring.docstringFormat": "google",
}


## 参考
[pep8 が pycodestyle に変わった話](https://qiita.com/tell-k/items/da52229749a7242b4440)  
[VSCodeのPython開発環境でpylintの代わりにflake8を導入し自動整形を設定する](https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb)  
[VS Code コーディング規約を快適に守る](https://qiita.com/firedfly/items/00c34018581c6cec9b84)