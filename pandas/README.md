# pandas

## 概要
覚書である。順次記載予定。

### 詳細

- dataframeで改行コードを制御してCSV出力する時  
```
df.to_csv('test.csv', line_terminator='\r\n')
```

## 参考
[pandas.DataFrameに列や行を追加](https://note.nkmk.me/python-pandas-assign-append/)  
[pandas.DataFrame, Seriesを時系列データとして処理](https://note.nkmk.me/python-pandas-time-series-datetimeindex/)  
[pandasで特定の文字列を含む行を抽出（完全一致、部分一致）](https://note.nkmk.me/python-pandas-str-contains-match/)
[Select Date And Time Ranges](https://chrisalbon.com/machine_learning/preprocessing_dates_and_times/select_date_and_time_ranges/)  
[pandasのDataFrameから期間を範囲指定して抽出する](https://qiita.com/terafon/items/6ec1ab28dcb261db2c73)  
[Pandas.DataFrameのメモリサイズを削減する（最大で8分の1）](https://qiita.com/nannoki/items/2a8934de31ad2258439d)  
