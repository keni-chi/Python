# pytest

## 概要
覚書である。順次記載予定。

### pytest -v --cov=src
```
----------- coverage: platform win32, python 3.6.4-final-0 -----------
Name          Stmts   Miss  Cover
---------------------------------
src\main.py       8      1    88%
```

### pytest -v --cov=src --cov-report=html
```
----------- coverage: platform win32, python 3.6.4-final-0 -----------
Coverage HTML written to dir htmlcov

### pytest -v --cov=src --cov-report=term-missing
----------- coverage: platform win32, python 3.6.4-final-0 -----------
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
src\main.py       8      1    88%   10
```

### pytest -vv -s --duration=0 --capture=sys --cov=src --cov-report=html
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

### pytest -vv -s --duration=0 --capture=sys --html=report.html
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

### pytest -vv -s -m test01 --duration=0 --capture=sys --html=report.html
markしたテストだけ実行
```
------- generated html file: C:\xxxxxxxxxxx\report.html ---
=========================== slowest test durations ========================
0.00s call     tests/test_main.py::TestCalc::test_add_01
0.00s teardown tests/test_main.py::TestCalc::test_add_01
0.00s setup    tests/test_main.py::TestCalc::test_add_01
```

### 意味
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
