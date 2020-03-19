# ABテストの検定ツール
2郡のデータでχ二乗検定もしくはフィッシャーの正確確率検定とグラフ作成を行います。

## 環境
|package|ver.|
|:--|:--|
|python |3.7.5 |
|numpy |1.18.1 |
|pandas |1.0.1 |
|scipy |1.4.1 |
|matplotlib |3.2.0 |
|seaborn |0.10.0 |

## インストール方法
```
pip install numpy
pip install pandas
pip install scipy
pip install matplotlib
pip install seaborn
```

## 実行方法
1. csvデータを用意
2. `py ABTestAnalysis.py`　もしくは　[ここ](https://github.com/Kahiro-M/ABTestAnalysis/releases/tag/Ver.1.0.0)からダウンロードしたexeを実行
3. 生成されたresult.htmlを開く

## 入力データの形式
### ファイル名
- A.csv
- b.csv

### データ構造
A.csvのデータ構造（例）
|No.|ラベル(任意の文字列)|データ(実数)|備考|
|:--|:--|:--|:--|
|1|A_user|A_data|この行は変更不可|
|2|hoge |1 |
|3|hogehoge |0 |
|4|hogehogehoge |1 |
|5... |...|...|

B.csvのデータ構造（例）
|No.|ラベル(任意の文字列)|データ(実数)|備考|
|:--|:--|:--|:--|
|1|B_user|B_data|この行は変更不可|
|2|fuga |0 |
|3|fugafuga |0 |
|4|fugafugafuga |1 |
|5... |...|...|