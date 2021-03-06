# pytest

## 概要
覚書である。順次記載予定。

### コマンド

#### pytest -v --cov=src
```
----------- coverage: platform win32, python 3.6.4-final-0 -----------
Name          Stmts   Miss  Cover
---------------------------------
src\main.py       8      1    88%
```

#### pytest -v --cov=src --cov-report=html
```
----------- coverage: platform win32, python 3.6.4-final-0 -----------
Coverage HTML written to dir htmlcov

### pytest -v --cov=src --cov-report=term-missing
----------- coverage: platform win32, python 3.6.4-final-0 -----------
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
src\main.py       8      1    88%   10
```

#### pytest -vv -s --duration=0 --capture=sys --cov=src --cov-report=html
カバレッジ出力
```
----------- coverage: platform win32, python 3.6.4-final-0 -----------
Coverage HTML written to dir htmlcov
=========================== slowest test durations =====================
0.00s setup    tests/test_main.py::TestCalc::test_add_02
0.00s call     tests/test_main.py::TestCalc::test_add_01
0.00s teardown tests/test_main.py::TestCalc::test_add_02
0.00s teardown tests/test_main.py::TestCalc::test_add_01
0.00s setup    tests/test_main.py::TestCalc::test_add_01
```

#### pytest -vv -s --duration=0 --capture=sys --html=report.html
レポート出力
```
------- generated html file: C:\xxxxxxxxxxx\report.html ---
=========================== slowest test durations ========================
0.00s setup    tests/test_main.py::TestCalc::test_add_02
0.00s call     tests/test_main.py::TestCalc::test_add_01
0.00s teardown tests/test_main.py::TestCalc::test_add_02
0.00s teardown tests/test_main.py::TestCalc::test_add_01
0.00s setup    tests/test_main.py::TestCalc::test_add_01
```

#### pytest -vv -s -m test01 --duration=0 --capture=sys --html=report.html
markしたテストだけ実行
```
------- generated html file: C:\xxxxxxxxxxx\report.html ---
=========================== slowest test durations ========================
0.00s call     tests/test_main.py::TestCalc::test_add_01
0.00s teardown tests/test_main.py::TestCalc::test_add_01
0.00s setup    tests/test_main.py::TestCalc::test_add_01
```


#### 意味  
- s  
  print文を出力  
- v  
  差分詳細表示  
- --duration=0   
  テストコードの定義関数ごとの時間を表示  
- Stmts   
  実行対象コード全体の行数  
- Miss   
  網羅できなかった行数  
- Cover   
  カバレッジ率  
- Missing  
  網羅されなかった行番号  


### pytest.ini
pytestのオプションなどを設定しておくことができる。


### .coveragerc
カバレッジ計測のルールを設定。   
カバレッジ計測を行わないファイルや行を定義するなど。   
参考: https://qiita.com/giginet/items/1f965ba6d8077f6399b8


### tox.ini  
flake8-docstirngsの場合、以下例のようにtox.iniを作成する。  
```
[flake8]
max-line-length=400
ignore=D104
```

## 参考
[monkeypatch](http://thinkami.hatenablog.com/entry/2017/03/07/065903)
