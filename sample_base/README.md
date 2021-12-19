# powershellの実行コマンド
- 初期
powershell ./make.ps1 init

- フレームワーク更新時
powershell ./make.ps1 update


# ログ出力例

```
2021-12-19 18:32:36,481 - base_service.py - 22 - INFO - execute---------start
2021-12-19 18:32:36,481 - app_service.py - 18 - INFO - init---------start
2021-12-19 18:32:36,497 - app_service.py - 24 - INFO - init---------end
2021-12-19 18:32:36,497 - app_service.py - 27 - INFO - preprocessing---------start
2021-12-19 18:32:36,497 - app_service.py - 32 - INFO - preprocessing---------end
2021-12-19 18:32:36,497 - app_service.py - 35 - INFO - run---------start
2021-12-19 18:32:37,281 - base_service.py - 34 - ERROR - [code:fw001] サンプルfwエラーのメッセージ
Traceback (most recent call last):
  File "C:\xxx\fw\base_service.py", line 30, in execute
    self.run()
  File "C:\xxx\app_service.py", line 65, in run
    raise AppException('[code:app001] サンプルappエラーのメッセージ')
fw.error_util.AppException: [code:app001] サンプルappエラーのメッセージ
```
