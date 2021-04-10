# cprofile_snakeviz

pip install snakeviz
python -m cProfile -s cumulative app.py
python -m cProfile -o profiling.stats app.py
snakeviz profiling.stats



# 参考
[【Pythonメモ】モジュールのプロファイリング](https://qiita.com/Kento75/items/8b72d64884d7072eece2)
